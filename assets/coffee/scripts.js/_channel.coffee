do ($ = jQuery) ->
	$(document).ready ->
		if window.channelOpen == undefined
			window.channelOpen = true
			#channel = new goog.appengine.Channel( token )
			#socket = channel.open()
			#socket.onopen = makeReady
			#socket.onmessage = onMessage