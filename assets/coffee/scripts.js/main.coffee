###
Responsible for binding methods to events
###

cinder = window.cinder = (methods, namespace = 'general') ->
	if methods['ready']
		jQuery(document).on "ready.cinder.#{namespace}", methods['ready']
	if methods['init']
		jQuery(document).on "init.cinder.#{namespace}", methods['init']
	if methods['defaultState']
		jQuery(document).on "defaultState.cinder.#{namespace}", methods['defaultState']


loadSection = window.loadSection = (section, callback, data) ->
	if callback == undefined
		callback = (section) ->
	if data == undefined
		data = {}

	data['section'] = section
	method = 'get_section'
	$.get( "api/#{method}/", data, (data) ->
		column = data.column
		$(".section[data-section-id='#{section}']").remove()
		$(".sidebar-link[data-section-id='#{section}']").remove()
		$(data['section']).appendTo(".column-#{column} .column-content").hide().slideDown()
		$(".section[data-section-id='#{section}']").cinder()
		callback($(".section[data-section-id='#{section}']"))
	)

if typeof(window.hasExecutedCache) == 'undefined'
	console.log('Running startup scripts')
	window.hasExecutedCache = {}

	window.hasExecuted = (name) ->
		if name not of window.hasExecutedCache
			window.hasExecutedCache[name] = 0

		window.hasExecutedCache[name] = window.hasExecutedCache[name] + 1
		return window.hasExecutedCache[name] - 1

jQuery(document).ready () ->
	jQuery('.cinder-cntr').cinder()



###
Main methods
###

do ($ = jQuery, window, document) -> # http://snippi.com/s/dp5g8iw

	methods = {}

	methods.init = () ->
		$(this).trigger "init.cinder", this
		$(this).trigger "defaultState.cinder", this
		return this

	# Adds plugin object to jQuery
	$.fn.extend
		cinder: (method) ->
			if methods[method]
				args =  Array.prototype.slice.call arguments, 1
				return methods[method].apply this, args
			else if typeof method is 'object' or not method
				return methods.init.apply this, arguments
			else
				console.error 'Cinder call failed', method, methods





do ($ = jQuery) ->

	makeReady = ->
		console.log('Channel opened')
		$('.loading-overlay').fadeOut()

	openChannel = ->
		channel = new goog.appengine.Channel( token )
		socket = channel.open()
		socket.onopen = makeReady
		socket.onmessage = onMessage

	sendMessage = (method, data) ->
		$.get( "api/#{method}/", data, (data) ->
			console.log(data)
			updateLiveFields(data)
		)

	updateLiveFields = (data) ->
		for key, value of data
			$(".live-field-html[data-field='#{key}']").html(value).effect("highlight", {}, 1500);
			$(".live-field-bool[data-field='#{key}']").attr('data-live-field-value', value)
			$(".live-field-visible[data-field='#{key}']").each(->
				if value
					$(@).removeClass('hidden')
				else
					$(@).addClass('hidden')
			)

	onMessage = (message) ->
		console.log(message)

	bindMessageButtons = ->
		$('.button.send-message').click ->
			method = $(@).attr('data-message')
			data = getDefaultData()
			sendMessage(method, data)

	bindSavedFields = ->
		$('.saved-field').each( ->
			id = $(@).attr('id')
			if window.localStorage["saved-field:#{id}"] != undefined
				$(@).val(window.localStorage["saved-field:#{id}"])
			$(@).blur(->
				id = $(@).attr('id')
				window.localStorage["saved-field:#{id}"] = $(@).val()
			)
		)

	getDefaultData = ->
		return {
			'ciphertext': $('#ciphertext').val(),
			'token': token
		}

	resetLiveFields = ->
		$('.live-field-html').each(->
			$(@).html($(@).attr('data-default'))
		)


	