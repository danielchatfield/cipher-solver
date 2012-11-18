do ($ = jQuery, window, document) ->

	methods = {}
	namespace = 'cinderSavedFields'
	selector = '.cinder-saved-field'

	methods.init = (e, cinder) ->
		if Modernizr.localstorage
			$(cinder).each () ->
				$elems = $(this).find( selector )
				$.merge $elems, $(this).filter( selector )
				$elems.on "change.cinder.#{namespace}", methods.change
				$elems.on "reset.cinder.#{namespace}", methods.reset
				$elems.trigger "reset"

	methods.change = (e) ->
		id = $(@).attr('id')
		if( $(@).attr('type') == 'checkbox' )
			value = $(@).prop('checked')
		else
			value = $(@).val()
		window.localStorage["saved-field:#{id}"] = value

	methods.reset = (e) ->
		id = $(@).attr('id')
		if window.localStorage["saved-field:#{id}"] != undefined
			value = window.localStorage["saved-field:#{id}"]
			if( $(@).attr('type') == 'checkbox' )
				$(@).prop('checked', value )
			else
				$(@).val(value)

			$(@).effect("highlight", {}, 1500)


	cinder methods, namespace