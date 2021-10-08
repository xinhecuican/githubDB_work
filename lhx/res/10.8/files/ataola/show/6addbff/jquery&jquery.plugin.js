/*
 * @Author: ataola
 * @Date: 2020-11-22 17:08:19
 * @Last Modified by: ataola
 * @Last Modified time: 2020-11-22 17:46:03
 */
'use strict';
(function ($) {
  $.fn.printStyle = function (options) {
    console.log('function printStyle start ========>');
    const el = this;
    const defaults = {
      color: 'red'
    };
    $.extend(true, defaults, options);
    const style = $(el).get(0).style;
    const div = document.createElement('div');
    for (const attr in style) {
      const val = getStyle($(el).get(0), attr);
      if (!(val instanceof Function)) {
        const res = `${attr}: ${val}`;
        div.innerHTML = div.innerHTML + res + '<br/>';
        console.log(res);
      }
    }
    document.body.appendChild(div);
    console.log('function printStyle end <========');
  };

  function getStyle(obj, attr) {
    if (obj.currentStyle) {
      return obj.currentStyle[attr];
    } else {
      return getComputedStyle(obj, false)[attr];
    }
  }
})(jQuery);
