var d = new Date();

var month=new Array("января","февраля","марта","апреля","мая","июня",
"июля","августа","сентября","октября","ноября","декабря");

document.write(' - ' + (1 + d.getHours()) +' ч. ' +d.getMinutes() + ' мин. ' +d.getDate() + ' ' +
    month[d.getMonth()] + ' ' + d.getFullYear() + ' г.');