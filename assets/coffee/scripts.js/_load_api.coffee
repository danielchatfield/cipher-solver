do ($ = jQuery, window, document) ->

	methods = {}
	namespace = 'cinderLoadApi'
	selector = '.button[data-method="load_api"]'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.click(methods.click)

	methods.click = () ->
		method = $(@).attr('data-api-method')
		options = $('#options').serialize()
		data = {
			'input': $('.input-cntr[data-input="active"] .actual-input').val()			
		}
		target = $(@).parents('.live-zone-cntr').find('.live-zone')
		$.post( "api/#{method}/?#{options}", data, (data) ->
			$(target).html('')
			$(target).html(data.output)
			$(target).effect("highlight", {}, 1500)
			$(target).cinder()

		)


	cinder methods, namespace