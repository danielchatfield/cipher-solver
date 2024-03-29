// Generated by CoffeeScript 1.4.0

/*
Responsible for binding methods to events
*/


(function() {
  var cinder, loadSection,
    __indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  cinder = window.cinder = function(methods, namespace) {
    if (namespace == null) {
      namespace = 'general';
    }
    if (methods['ready']) {
      jQuery(document).on("ready.cinder." + namespace, methods['ready']);
    }
    if (methods['init']) {
      jQuery(document).on("init.cinder." + namespace, methods['init']);
    }
    if (methods['defaultState']) {
      return jQuery(document).on("defaultState.cinder." + namespace, methods['defaultState']);
    }
  };

  loadSection = window.loadSection = function(section, callback, data) {
    var method;
    if (callback === void 0) {
      callback = function(section) {};
    }
    if (data === void 0) {
      data = {};
    }
    data['section'] = section;
    method = 'get_section';
    return $.get("api/" + method + "/", data, function(data) {
      var column;
      column = data.column;
      $(".section[data-section-id='" + section + "']").remove();
      $(".sidebar-link[data-section-id='" + section + "']").remove();
      $(data['section']).appendTo(".column-" + column + " .column-content").hide().slideDown();
      $(".section[data-section-id='" + section + "']").cinder();
      return callback($(".section[data-section-id='" + section + "']"));
    });
  };

  if (typeof window.hasExecutedCache === 'undefined') {
    console.log('Running startup scripts');
    window.hasExecutedCache = {};
    window.hasExecuted = function(name) {
      if (!(name in window.hasExecutedCache)) {
        window.hasExecutedCache[name] = 0;
      }
      window.hasExecutedCache[name] = window.hasExecutedCache[name] + 1;
      return window.hasExecutedCache[name] - 1;
    };
  }

  jQuery(document).ready(function() {
    return jQuery('.cinder-cntr').cinder();
  });

  /*
  Main methods
  */


  (function($, window, document) {
    var methods;
    methods = {};
    methods.init = function() {
      $(this).trigger("init.cinder", this);
      $(this).trigger("defaultState.cinder", this);
      return this;
    };
    return $.fn.extend({
      cinder: function(method) {
        var args;
        if (methods[method]) {
          args = Array.prototype.slice.call(arguments, 1);
          return methods[method].apply(this, args);
        } else if (typeof method === 'object' || !method) {
          return methods.init.apply(this, arguments);
        } else {
          return console.error('Cinder call failed', method, methods);
        }
      }
    });
  })(jQuery, window, document);

  (function($) {
    var bindMessageButtons, bindSavedFields, getDefaultData, makeReady, onMessage, openChannel, resetLiveFields, sendMessage, updateLiveFields;
    makeReady = function() {
      console.log('Channel opened');
      return $('.loading-overlay').fadeOut();
    };
    openChannel = function() {
      var channel, socket;
      channel = new goog.appengine.Channel(token);
      socket = channel.open();
      socket.onopen = makeReady;
      return socket.onmessage = onMessage;
    };
    sendMessage = function(method, data) {
      return $.get("api/" + method + "/", data, function(data) {
        console.log(data);
        return updateLiveFields(data);
      });
    };
    updateLiveFields = function(data) {
      var key, value, _results;
      _results = [];
      for (key in data) {
        value = data[key];
        $(".live-field-html[data-field='" + key + "']").html(value).effect("highlight", {}, 1500);
        $(".live-field-bool[data-field='" + key + "']").attr('data-live-field-value', value);
        _results.push($(".live-field-visible[data-field='" + key + "']").each(function() {
          if (value) {
            return $(this).removeClass('hidden');
          } else {
            return $(this).addClass('hidden');
          }
        }));
      }
      return _results;
    };
    onMessage = function(message) {
      return console.log(message);
    };
    bindMessageButtons = function() {
      return $('.button.send-message').click(function() {
        var data, method;
        method = $(this).attr('data-message');
        data = getDefaultData();
        return sendMessage(method, data);
      });
    };
    bindSavedFields = function() {
      return $('.saved-field').each(function() {
        var id;
        id = $(this).attr('id');
        if (window.localStorage["saved-field:" + id] !== void 0) {
          $(this).val(window.localStorage["saved-field:" + id]);
        }
        return $(this).blur(function() {
          id = $(this).attr('id');
          return window.localStorage["saved-field:" + id] = $(this).val();
        });
      });
    };
    getDefaultData = function() {
      return {
        'ciphertext': $('#ciphertext').val(),
        'token': token
      };
    };
    return resetLiveFields = function() {
      return $('.live-field-html').each(function() {
        return $(this).html($(this).attr('data-default'));
      });
    };
  })(jQuery);

  (function($) {
    return $(document).ready(function() {
      if (window.channelOpen === void 0) {
        return window.channelOpen = true;
      }
    });
  })(jQuery);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderClearColumn';
    selector = '.button[data-method="clear_column"]';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.dblclick(methods.dblclick);
      });
    };
    methods.dblclick = function() {
      return $(this).parents('.column').find('.column-content').html('');
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderLoadCryptanalysis';
    selector = '.section-cryptanalysis';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.find('.button[data-method="do_section"]').click(methods.click).removeClass('hidden');
      });
    };
    methods.click = function() {
      var data, method, options, section;
      method = $(this).parents('.section').attr('data-section-name');
      options = $('#options').serialize();
      data = {
        'input': $('.input-cntr[data-input="active"] .actual-input').val()
      };
      section = $(this).parents('.section').find('.section-content');
      return $.post("api/" + method + "/?" + options, data, function(data) {
        var key, value, _ref, _ref1, _ref2, _ref3;
        $(section).html('');
        _ref = data.output;
        for (key in _ref) {
          value = _ref[key];
          if (__indexOf.call(data.objects.bool_values, key) >= 0) {
            $("<div class='info-box live-field-bool' data-live-field-value='" + value + "'>" + key + "</div>").appendTo(section);
          }
        }
        $("<div class='divider'></div>").appendTo(section);
        _ref1 = data.output;
        for (key in _ref1) {
          value = _ref1[key];
          if (__indexOf.call(data.objects.num_values, key) >= 0) {
            $("<div class='info-box'><div class='info-box-number'>" + value + "</div>" + key + "</div>").appendTo(section);
          }
        }
        $("<div class='divider'></div>").appendTo(section);
        _ref2 = data.output;
        for (key in _ref2) {
          value = _ref2[key];
          if (__indexOf.call(data.objects.html_values, key) >= 0) {
            $("<div class='info-box info-box-html'>" + value + "</div>").appendTo(section);
          }
        }
        _ref3 = data.output;
        for (key in _ref3) {
          value = _ref3[key];
          if (__indexOf.call(data.objects.num_values, key) >= 0) {
            continue;
          }
          if (__indexOf.call(data.objects.bool_values, key) >= 0) {
            continue;
          }
          if (__indexOf.call(data.objects.html_values, key) >= 0) {
            continue;
          }
          console.log('Unhandled cryptanalysis key:' + key, value);
        }
        $(section).effect("highlight", {}, 1500);
        return $(section).cinder();
      });
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderLoadSectionButtons';
    selector = '.tray .button.load-section';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.on("click.cinder." + namespace, methods.click);
      });
    };
    methods.click = function(e) {
      var parent_section, section;
      section = $(this).attr('data-section');
      parent_section = $(this).parents('.sections').attr('data-section-id');
      return loadSection(section, function(section) {
        return $(this).data('cinder-parent', parent_section);
      });
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($) {
    return $(document).ready(function() {
      if (!$('body').hasClass('loaded')) {
        $('body').addClass('loaded');
        return loadSection('input', function() {
          $('.loading-overlay').fadeOut();
          return $('#section-input').attr('data-input', 'active');
        });
      }
    });
  })(jQuery);

  (function($, window, document) {
    return $(document).ready(function() {
      if (!hasExecuted('_reload_app')) {
        $('<div class="topbar-link">Reload</div>').appendTo('.topbar').click(function() {
          return location.reload();
        });
        $('<div class="topbar-link">Reload Styles</div>').appendTo('.topbar').click(function() {
          var queryString;
          queryString = '?reload=' + new Date().getTime();
          return $('link[rel="stylesheet"]').each(function() {
            return this.href = this.href.replace(/\?.*|$/, queryString);
          });
        });
        if (Modernizr.localstorage) {
          return $('<div class="topbar-link">Clear localStorage</div>').appendTo('.topbar').click(function() {
            return window.localStorage.clear();
          });
        }
      }
    });
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderSavedFields';
    selector = '.cinder-saved-field';
    methods.init = function(e, cinder) {
      if (Modernizr.localstorage) {
        return $(cinder).each(function() {
          var $elems;
          $elems = $(this).find(selector);
          $.merge($elems, $(this).filter(selector));
          $elems.on("change.cinder." + namespace, methods.change);
          $elems.on("reset.cinder." + namespace, methods.reset);
          return $elems.trigger("reset");
        });
      }
    };
    methods.change = function(e) {
      var id, value;
      id = $(this).attr('id');
      if ($(this).attr('type') === 'checkbox') {
        value = $(this).prop('checked');
      } else {
        value = $(this).val();
      }
      return window.localStorage["saved-field:" + id] = value;
    };
    methods.reset = function(e) {
      var id, value;
      id = $(this).attr('id');
      if (window.localStorage["saved-field:" + id] !== void 0) {
        value = window.localStorage["saved-field:" + id];
        if ($(this).attr('type') === 'checkbox') {
          $(this).prop('checked', value);
        } else {
          $(this).val(value);
        }
        return $(this).effect("highlight", {}, 1500);
      }
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderSelectInput';
    selector = '.button[data-method="select_input"]';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        $elems.click(methods.click);
        return $elems.each(function() {
          if ($(this).parents('.input-cntr').length = 0) {
            return;
          }
          if ($($(this).parents('.input-cntr')[0]).find('.actual-input').length > 0) {
            return $(this).removeClass('hidden');
          }
        });
      });
    };
    methods.click = function() {
      $('.input-cntr').attr('data-input', 'inactive');
      return $($(this).parents('.input-cntr')[0]).attr('data-input', 'active');
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderCloseSection';
    selector = '.button[data-method="close_section"]';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.dblclick(methods.dblclick);
      });
    };
    methods.dblclick = function() {
      return $(this).parents('.section').remove();
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderMinimizeSection';
    selector = '.button[data-method="minimize_section"]';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.click(methods.click);
      });
    };
    methods.click = function() {
      var $section;
      $section = $(this).parents('.section');
      if ($section.hasClass('section-minimized')) {
        $section.removeClass('section-minimized');
        $section.find('.section-content').slideDown();
        return $(this).html('Minimize');
      } else {
        $section.addClass('section-minimized');
        $section.find('.section-content').slideUp();
        return $(this).html('Restore');
      }
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderLoadSample';
    selector = '.target-load_sample';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.parents('.section').find('.button[data-method="load_sample"]').click(methods.click).removeClass('hidden');
      });
    };
    methods.click = function() {
      var data, method, sample_name, section, target;
      sample_name = '';
      method = 'load_sample';
      target = $(this).parents('.section').find('.target-load_sample');
      section = $(this).parents('.section').attr('data-section-id');
      if (Modernizr.localstorage) {
        if (window.localStorage["prompt/load_sample/" + section] !== void 0) {
          sample_name = window.localStorage["prompt/load_sample/" + section];
        } else {
          sample_name = window.localStorage["prompt/load_sample"];
        }
      }
      sample_name = prompt('Enter sample name', sample_name);
      if (sample_name === null) {
        return;
      }
      if (Modernizr.localstorage) {
        window.localStorage["prompt/load_sample/" + section] = window.localStorage["prompt/load_sample"] = sample_name;
      }
      data = {
        'sample_name': sample_name
      };
      return $.get("api/" + method + "/", data, function(data) {
        $(target).val(data.output).change();
        return $(target).effect("highlight", {}, 1500);
      });
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderLoadSectionButtons';
    selector = '.button[data-method="load_section"]';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.click(methods.click);
      });
    };
    methods.click = function() {
      var section;
      section = $(this).attr('data-section');
      return loadSection(section);
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderLoadSectionButtons';
    selector = '.button[data-method="load_custom_section"]';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.click(methods.click);
      });
    };
    methods.click = function() {
      var column, data, section;
      if ($(this).parents('.sidebar').hasClass('sidebar-left')) {
        column = 'left';
      } else {
        column = 'right';
      }
      if (Modernizr.localstorage) {
        section = window.localStorage['prompt/loadsection/' + column];
      }
      section = prompt('Enter section name', section);
      if (section === null) {
        return;
      }
      if (Modernizr.localstorage) {
        window.localStorage['prompt/loadsection/' + column] = section;
      }
      data = {
        'column': column
      };
      return loadSection(section, void 0, data);
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderTipTip';
    selector = '.tiptip';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems, options;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        options = {
          'delay': 0,
          'fadeIn': 0,
          'fadeOut': 0,
          'attribute': 'data-title',
          'defaultPosition': 'top'
        };
        return $elems.tipTip(options);
      });
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

  (function($, window, document) {
    var methods, namespace, selector;
    methods = {};
    namespace = 'cinderLoadApi';
    selector = '.button[data-method="load_api"]';
    methods.init = function(e, cinder) {
      return $(cinder).each(function() {
        var $elems;
        $elems = $(this).find(selector);
        $.merge($elems, $(this).filter(selector));
        return $elems.click(methods.click);
      });
    };
    methods.click = function() {
      var data, method, options, target;
      method = $(this).attr('data-api-method');
      options = $('#options').serialize();
      data = {
        'input': $('.input-cntr[data-input="active"] .actual-input').val()
      };
      target = $(this).parents('.live-zone-cntr').find('.live-zone');
      return $.post("api/" + method + "/?" + options, data, function(data) {
        $(target).html('');
        $(target).html(data.output);
        $(target).effect("highlight", {}, 1500);
        return $(target).cinder();
      });
    };
    return cinder(methods, namespace);
  })(jQuery, window, document);

}).call(this);
