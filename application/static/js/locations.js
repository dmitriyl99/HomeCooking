function init(){let e=new ymaps.control.SearchControl({options:{size:"large",provider:"yandex#seacrh"}}),t=new ymaps.Map("map",{center:[41.26465,69.21627],zoom:12,controls:[e,"fullscreenControl","zoomControl"]}),n=document.querySelectorAll(".location-item"),o=[],s=[];n.forEach(e=>{let t=e.getElementsByClassName("latitude")[0].innerHTML,n=e.getElementsByClassName("longitude")[0].innerHTML,l=e.getElementsByClassName("address")[0].innerHTML;o.push([t,n]),s.push(l)});let l=[];for(let e=0;e<o.length;e++)l[e]=new ymaps.GeoObject({geometry:{type:"Point",coordinates:o[e]},properties:{clusterCaption:"Заказ № "+(e+1),balloonContentBody:s[e],hintContent:s[e]}},{preset:"islands#orangeDotIcon"});let r=new ymaps.Clusterer({clusterDisableClickZoom:!0,preset:"islands#orangeClusterIcons"});r.add(l),t.geoObjects.add(r)}ymaps.ready(init);