do ($ = jQuery, window, document) ->

	methods = {}
	namespace = 'cinderLoadCryptanalysis'
	selector = '.section-cryptanalysis'

	methods.init = (e, cinder) ->
		$(cinder).each () ->
			$elems = $(this).find( selector )
			$.merge $elems, $(this).filter( selector )
			$elems.find('.button[data-method="do_section"]').click(methods.click).removeClass('hidden')

	methods.click = () ->
		method = $(@).parents('.section').attr('data-section-name')
		options = $('#options').serialize()
		data = {
			'input': $('.section[data-input="active"] .actual-input').val()			
		}
		section = $(@).parents('.section').find('.section-content')
		$.post( "api/#{method}/?#{options}", data, (data) ->
			$(section).html('')

			for key, value of data.output
				if key in data.objects.bool_values
					$("<div class='info-box live-field-bool' data-live-field-value='#{value}'>#{key}</div>").appendTo(section)
			$("<div class='divider'></div>").appendTo(section)
			for key, value of data.output	
				if key in data.objects.num_values
					$("<div class='info-box'><div class='info-box-number'>#{value}</div>#{key}</div>").appendTo(section)
			$("<div class='divider'></div>").appendTo(section)

			for key, value of data.output	
				if key in data.objects.html_values
					$("<div class='info-box info-box-html'>#{value}</div>").appendTo(section)

			for key, value of data.output
				if key in  data.objects.num_values
					continue
				if key in  data.objects.bool_values
					continue
				if key in  data.objects.html_values
					continue
				console.log('Unhandled cryptanalysis key:' + key, value)

			$(section).effect("highlight", {}, 1500)

			$(section).cinder()

		)


	cinder methods, namespace