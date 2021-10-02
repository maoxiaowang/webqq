function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = $.cookie('csrftoken');

var activeElement;
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  }
);
$(document).ajaxStart(
  function (e) {
    try {
      activeElement = $(e.target.activeElement);
      // just a precautionary check
      if (!activeElement.hasClass('btn')) {
        return
      }
      activeElement.attr('disabled', true)
    } catch (ex) {
      console.log(ex);
    }
  }
).ajaxStop(
  function () {
    if (activeElement) {
      try {
        if (!activeElement.hasClass('btn')) {
          return
        }
        activeElement.removeAttr('disabled')
      } catch (ex) {
        console.log(ex);
      }
    }

  }
).ajaxSuccess(
  function (event, xhr, options) {
    if (xhr.responseJSON &&
      // options.type !== 'GET' &&
      xhr.responseJSON.result === false) {
      let res = xhr.responseJSON;
      $.each(res.messages, function () {
        let msg = this;
        if (res.result) {
          toastr.success(msg);
        } else {
          toastr.error(msg)
        }
      });
    } else {

    }
  }
).ajaxError(
  function (event, xhr, options, exc) {
    let statusText = xhr.statusText;
    if (xhr.status === 0) {
      statusText = 'Disconnected from server'
    }
    toastr.error(statusText)
  }
);



function getUrlParam(key) {

    // 获取参数

    var url = window.location.search;

    // 正则筛选地址栏

    var reg = new RegExp("(^|&)" + key + "=([^&]*)(&|$)");

    // 匹配目标参数

    var result = url.substr(1).match(reg);

    //返回参数值

    return result ? decodeURIComponent(result[2]) : null;

}
