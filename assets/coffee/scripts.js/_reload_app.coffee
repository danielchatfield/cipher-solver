do ($ = jQuery, window, document) ->

	$(document).ready () ->
		if not hasExecuted('_reload_app')
			$('<div class="topbar-link">Reload</div>').appendTo('.topbar').click(->
				location.reload()
			)
			$('<div class="topbar-link">Reload Styles</div>').appendTo('.topbar').click(->
				queryString = '?reload=' + new Date().getTime();
				$('link[rel="stylesheet"]').each( () ->
					this.href = this.href.replace(/\?.*|$/, queryString)
				)
			)
			if Modernizr.localstorage
				$('<div class="topbar-link">Clear localStorage</div>').appendTo('.topbar').click(->
					window.localStorage.clear()
				)
