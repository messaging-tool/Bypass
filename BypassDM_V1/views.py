from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tweet, EncryptedMessage
from autho.models import TwitterUser
import tweepy
from django.urls import reverse
from django.conf import settings
from tweepy import OAuthHandler, API
from .forms import TweetForm
from autho.models import TwitterAuthToken, TwitterUser
import uuid
from cryptography.fernet import Fernet
from django.views.decorators.csrf import csrf_protect



SECRET_KEY = b'<045349f35b3d41e9b778798f1d4b561caf8084f4ba2640c3d9742ec6e960f6b6a7c3dc277ce4c1432cf0ad5ad1a8c3d5f99736afcafbf596ae6ea060348ceb55b13e869d6d>'


@login_required
@csrf_protect
def tweet_view(request):
    try:
        twitter_user = TwitterUser.objects.get(user=request.user)
    except TwitterUser.DoesNotExist:
        messages.error(request, 'Twitter user does not exist')
        return redirect('home')

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            # Get the Twitter user's access token and secret from the database
            auth = OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET)
            auth.set_access_token(twitter_user.twitter_oauth_token.oauth_token, twitter_user.twitter_oauth_token.oauth_token_secret)
            api = API(auth)

            # Get the username and message from the form
            username = form.cleaned_data['username']
            message = form.cleaned_data['message']

            # Encrypt the message using a randomly generated key
            key = Fernet.generate_key()
            f = Fernet(key)
            encrypted_message = f.encrypt(message.encode())
            str_encrypted_msg = encrypted_message.decode()

            # Construct the link with a unique UUID
            tweet_uuid = uuid.uuid4()
            link = f'https://BypassDMs.com/BypassDM_V1/private_message/{tweet_uuid}/'
            
            # ENCRYPT KEY
            key_string = key.decode()
            
            # Save the tweet to the database
            encrypted_message_obj = EncryptedMessage.objects.create(encrypted_message=encrypted_message, encrypted_text=str_encrypted_msg)
            tweet = Tweet.objects.create(twitter_user=twitter_user, username=username, twitter_user_fullname=twitter_user.name, key=key_string, link=link, twitter_userid=twitter_user.id, message=encrypted_message_obj)

            # Construct the tweet message
            # tweet_text = f'bcc @{username}! msg: {link}'
            
            tweet_text = f'Hey @{username}, I have a confidential message just for you. Bypass the cluttered DMs and access it securely on BypassDM. Visit {link} to unveil your exclusive message.'
            
            # Construct the Open Graph metadata
            og_title = 'From BypassDM-'
            og_description = 'A tool that bypasses twitter DMs limitations'
            og_url = link
            og_image = 'https://ibb.co/nP7SxWQ'

            # Construct the Twitter URL with pre-populated tweet and Open Graph metadata
            twitter_url = f'https://twitter.com/intent/tweet?text={tweet_text}&description={og_description}&image={og_image}'

            # Construct the Twitter URL with pre-populated tweet
#             twitter_url = f'https://twitter.com/intent/tweet?text={tweet_text}'

            # Redirect to Twitter for tweeting
            return redirect(twitter_url)
    else:
        form = TweetForm()
    return render(request, 'BypassDM_V1/tweet.html', {'form': form})

    
@login_required
def message_view(request, tweet_uuid):
    try:
        link_query = f'https://bypassdms.com/BypassDM_V1/private_message/{tweet_uuid}/'
        tweet = Tweet.objects.get(link__iexact=link_query)        
        if tweet.username.lower() == request.user.username.lower():
            # Decrypt the message using the Fernet module and the secret key
            # DECRYPT KEY
            key_byte = tweet.key.encode()
            # Decrypt the message using the Fernet module and the secret key
            f = Fernet(key_byte)
            byte_encrypted_msg = tweet.message.encrypted_text.encode()
            decrypted_message = f.decrypt(byte_encrypted_msg).decode()
            sender_username = tweet.twitter_user
            sender_fullame = tweet.twitter_user_fullname

            # Pass the decrypted message to the template
            return render(request, 'BypassDM_V1/message.html', {'message': decrypted_message, 'sender_username': sender_username, 'sender_fullname': sender_fullame})
        return render(request, 'BypassDM_V1/error.html', {'error_message': 'You are not authorized to view this message'})
    except Tweet.DoesNotExist:
        return render(request, 'BypassDM_V1/error.html', {'error_message': 'Message not found'})



# # @login_required
# # def message_view(request, tweet_uuid):
# #     try:
# #         tweet = Tweet.objects.get(link=f'https://BypassDM.com/private_message/{tweet_uuid}/')
# #         if tweet.username.lower() == request.user.username.lower():
# #             # Encrypt the message using the Fernet module and the secret key
# #             f = Fernet(SECRET_KEY)
# #             encrypted_message = f.encrypt(tweet.message.encode('utf-8'))

# #             # Pass the encrypted message to the template
# #             return render(request, 'BypassDM_V1/message.html', {'message': encrypted_message})
# #         else:
# #             return render(request, 'BypassDM_V1/error.html', {'error': 'You are not authorized to view this message'})
# #     except Tweet.DoesNotExist:
# #         return render(request, 'BypassDM_V1/error.html', {'error': 'Message not found'})

