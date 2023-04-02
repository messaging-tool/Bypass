var div=document.createElement("div");div.innerHTML=`<form class="newsletter-form" method="post" action="https://listmonk.cobratate.com/subscription/form" class="listmonk-form nl-form" style="text-align: center;">
    <div style="width:100%;">
        <input type="hidden" name="nonce" />
        <input class='form-input form-input-large' type="email" name="email" required placeholder="Your email address" /></p>
        <input type="text" name="name" placeholder="Your Name (optional)" class='form-input form-input-large' style="margin-top: 8px;" />
      
        <input style="display: none;" id="ba618" type="checkbox" name="l" checked value="ba618a07-f653-485e-93b1-09bd5e4c0a00" />

        <input type="submit" value="Subscribe" class='button-large bg-primary-3 w-button' style="margin-top: 16px; width: 300px;" />
    </div>
</form>`;document.currentScript.parentNode.insertBefore(div.firstElementChild,document.currentScript);