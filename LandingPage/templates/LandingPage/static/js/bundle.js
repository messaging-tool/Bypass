!function e(t,i,n){function r(o,a){if(!i[o]){if(!t[o]){var l="function"==typeof require&&require;if(!a&&l)return l(o,!0);if(s)return s(o,!0);var u=new Error("Cannot find module '"+o+"'");throw u.code="MODULE_NOT_FOUND",u}var c=i[o]={exports:{}};t[o][0].call(c.exports,(function(e){return r(t[o][1][e]||e)}),c,c.exports,e,t,i,n)}return i[o].exports}for(var s="function"==typeof require&&require,o=0;o<n.length;o++)r(n[o]);return r}({1:[function(e,t,i){var n,r;window.app.website=(n=app,r={menu:{$wrapper:null,$inner:null,timeoutId:null,show:function(){var e=this;this.$wrapper.hasClass("visible")||(n.$window.on("resize.menu orientationchange.menu",(function(){clearTimeout(e.timeoutId),e.timeoutId=setTimeout((function(){var t=n.$window.height(),i=e.$inner.height();e.$wrapper.hasClass("docked")?t>i&&e.$wrapper.removeClass("docked"):t<i&&e.$wrapper.addClass("docked"),setTimeout((function(){e.$wrapper.focus()}),50)}),25)})).trigger("resize.menu"),n.$body.css("overflow","hidden"),this.$wrapper.addClass("visible"),setTimeout((function(){e.$wrapper.focus()}),50))},hide:function(){this.$wrapper.removeClass("visible"),n.$body.css("overflow",""),n.$window.off("resize.menu").off("orientationchange.menu")},toggle:function(){this.$wrapper.hasClass("visible")?this.hide():this.show()},init:function(){var e=this;this.$wrapper=$("#menu").attr("tabindex","-1").on("click",'a[href="#menu"]',(function(t){t.preventDefault(),t.stopPropagation(),t.stopImmediatePropagation(),e.hide()})).on("click","a",(function(t){var i=$(this).attr("href");t.preventDefault(),t.stopPropagation(),e.hide(),setTimeout((function(){window.location.href=i}),350)})).on("click",(function(t){t.preventDefault(),t.stopPropagation(),e.hide()})).on("keydown",(function(t){27===t.keyCode&&e.hide()})),this.$inner=this.$wrapper.children(".inner").first(),n.$body.on("click",'a[href="#menu"]',(function(t){t.preventDefault(),t.stopPropagation(),e.toggle()}))}},docs:{excludes:[],list:[],multiwords:[],search:{$activeResult:null,$input:null,$results:null,$wrapper:null,gotoNextResult:function(){var e=this.$activeResult.next();0!=e.length&&(this.$activeResult.removeClass("active"),this.$activeResult=e,this.$activeResult.addClass("active"))},gotoPreviousResult:function(){var e=this.$activeResult.prev();0!=e.length&&(this.$activeResult.removeClass("active"),this.$activeResult=e,this.$activeResult.addClass("active"))},init:function(){var e=this,t=$(".sidebar > .inner"),i=$(".content");this.$wrapper=$(".search"),0!=this.$wrapper.length&&(this.$input=this.$wrapper.find("input").on("input",(function(t){var i,n=e.$input.val();i=r.docs.query(n),e.update(i)})).on("keydown",(function(t){var i=!1;switch(t.keyCode){case 38:e.gotoPreviousResult(),i=!0;break;case 40:e.gotoNextResult(),i=!0;break;case 13:e.openActiveResult(),i=!0;break;case 27:e.$input.blur(),i=!0}i&&(t.preventDefault(),t.stopPropagation())})),this.$results=$('<ul class="results empty"></ul>').insertAfter(this.$input),Breakpoints.on("<large",(function(){e.$wrapper.prependTo(i)})),Breakpoints.on(">medium",(function(){e.$wrapper.prependTo(t)})))},openActiveResult:function(){this.$input.blur(),this.$activeResult&&(window.location.href=this.$activeResult.children("a").attr("href"))},update:function(e){var t;if(this.$results.children().remove(),0==e.length)this.$results.addClass("empty"),this.$activeResult=null;else{for(this.$results.removeClass("empty"),t=0;t<e.length&&t<3;t++)this.$results.append("<li"+(0==t?' class="active"':"")+'><a href="/docs/'+e[t].url+'">'+e[t].title+"</a></li>");this.$activeResult=this.$results.find("li.active")}}},init:function(){var e,t,i,r,s;this.search.init(),0!=(s=$(".changelog")).length&&(e=s.find(".final"),t=s.attr("data-url"),i=!1,r=function(){var n=parseInt(e.prev().attr("data-index"));isNaN(n)||(i=!0,s.addClass("is-loading"),$.ajax({url:t+"?start="+(n+1),type:"GET",success:function(t){if(!t)return e.find("h2").text(s.attr("data-final-content")),void s.removeClass("is-loading");$(t).insertBefore(e),i=!1,s.removeClass("is-loading")}}))},n.$window.on("load scroll",(function(){var e=window.innerHeight;i||window.scrollY>=document.body.scrollHeight-window.innerHeight-e&&r()})))},load:function(e){this.list=e.list,this.multiwords=e.multiwords,this.excludes=e.excludes},query:function(e){var t,i,n,r,s,o=[];if((i=e.replace(/\s+/," ").trim().split(" ")).length>1)for(n of this.excludes)-1!=(r=i.indexOf(n))&&delete i[r];if(0==i.length)return o;for(n of(e=Object.values(i).join(" "),this.multiwords))e=e.replace(n,n.replace(" ","-"),e);for(n in i=e.split(" "))i[n]=i[n].replace("-"," ");for(n of this.list){for(r of(s=0,i))if(0!=r.length)for(t of n.keywords)if(t.substr(0,r.length)==r){s++;break}s==i.length&&o.push(n)}return o}},init:function(e){switch(r.menu.init(),n.$body.data("action")){case"index":$('[href="#about"]').on("click",(function(e){var t=$(this).attr("href"),i=$(t).find("header").offset().top-.1*n.$window.height();e.stopPropagation(),e.preventDefault(),$(this).blur(),$("body,html").stop().animate({scrollTop:i},1e3,"swing")})),n.scrollify($(".carousel")),n.scrollify($(".highlight.simple"),{middle:!0,delay:125,offset:25,duration:5e3,replay:!0}),n.scrollify($(".highlight.responsive"),{middle:!0,delay:125,offset:25,duration:5e3,replay:!0}),n.scrollify($(".highlight.free"),{middle:!0,delay:125,offset:25,duration:6e3,replay:!0});break;case"contact":case"verify":case"login":n.enableReCAPTCHA("form");break;case"signup":case"reset":n.enableReCAPTCHA("form","alternate");break;case"docs":r.docs.init()}}})},{}]},{},[1]);