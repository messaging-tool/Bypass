$(document).ready(function(){'use strict';$('.menu > ul > li:has( > ul)').addClass('menu-dropdown-icon');$('.menu > ul > li > ul:not(:has(ul))').addClass('normal-sub');if(window.location.href.indexOf('product')>-1){$('.menu > ul').before('<a href="../index.html" class="menu-mobile"><img src="../images/Tate-Logo-Web3.png" alt="Tate logo" /></a>');}else{$('.menu > ul').before('<a href="index.html" class="menu-mobile"><img src="images/Tate-Logo-Web3.png" alt="Tate logo" /></a>');}
$('.menu > ul > li').hover(function(e){if($(window).width()>1230){$(this).children('ul').fadeIn(150);e.preventDefault();}},function(e){if($(window).width()>1230){$(this).children('ul').fadeOut(150);e.preventDefault();}});$(document).on('click',function(e){if($(e.target).parents('.menu').length===0)
$('.menu > ul').removeClass('show-on-mobile');});$('.menu > ul > li').click(function(){var thisMenu=$(this).children('ul');var prevState=thisMenu.css('display');$('.menu > ul > li > ul').fadeOut();if($(window).width()<1230){if(prevState!=='block')thisMenu.fadeIn(150);$(this).toggleClass('rotate');}});$('.menu-mobile').click(function(e){$('.menu > ul').toggleClass('show-on-mobile');$('.menu-mobile').toggleClass('close-btn');e.preventDefault();});});