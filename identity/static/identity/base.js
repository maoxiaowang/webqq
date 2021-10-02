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
      statusText = gettext('Disconnected from server')
    }
    toastr.error(statusText)
  }
);
