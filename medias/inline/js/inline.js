var quick_edit_mode = false;
function launch_dialog()
{
    //Can't user "this" in event function
    var el = $(this);
    //Define the position of the block
    var offset = $(this).offset();
    var scroll_top = $('body').scrollTop();
    var scroll_left = $('body').scrollLeft();
    var pos_left = offset.left - scroll_left;
    var pos_top = offset.top - scroll_top;
    //Function for submit event
    var form_submit = function()
    {
        //Options for ajax call
    	var options = {
    		target : el,
    		success : function()
    		{
        		remove_dialog();            		  
    		}
    	};
    	//Submit form by ajax
    	$('#django_inline').ajaxSubmit(options);
    	return false;
    }
    var remove_dialog = function()
    {
//    		$("#dialog").dialog('close');
//    		$("#dialog").dialog('destroy');
        $("#dialog").remove();
//    		quick_edit_mode = false;   
        toggle_quick_edit_mode({mode: false});
    }
    if($('#dialog').length != 0)
        $("#dialog").remove();
    //Create a div and load form from server
    //Fonction callback is adding submit event
    $('<div>').attr('id','dialog').appendTo("body").load('/django_inline/widget/' + $(this).attr('id'), {}, function() {
            $('#django_inline').submit(form_submit)
        });
	$("#dialog").dialog({
        bgiframe: true,
        autoOpen: true,
        dialogClass: 'quick_edit_box',
        minHeight: 100,
        title: "Vit'édit",
        resizable: true,
        zindex: 10000,
//        modal: true,
        stack: true,
        position: [pos_left, pos_top],
        buttons: {
            'Ok': function() {
                $('#django_inline').submit();
            },
            Cancel: function(){
                remove_dialog()    
            }
        },
		close: function() {
    		remove_dialog();
		}
	});		
}
/*
*   Activate the quick edit
*   @param  target   jquery queryset to consider
*/
function activate_quick_edit(options)
{
    options = $.extend({
        target:  $('.editable')
        }, options || {});
    if(!quick_edit_mode)
    {
        options.target.unbind('click');
        options.target.parents('a').unbind("click");
        options.target.removeClass('active_edit');
    }
    else
    {
        options.target.click(launch_dialog);
        options.target.addClass('active_edit');
        options.target.parents('a').bind("click", function(event) {
            event.preventDefault();event.stopPropagation();
        });
//		var parentEls = $('.editable').parents('a').map(function() {return this.tagName;}).get().join(', ');
//		alert(parentEls);
/*		$('.editable').parents('a').bind("click", function(event) {
            event.preventDefault();event.stopPropagation();
            if(event.currentTarget.nodeName == 'A')
            {
                alert(event.target.nodeName+ ' '+event.currentTarget.nodeName);
            }
        }
        );*/
	}
//    quick_edit_mode = !quick_edit_mode;
}
function toggle_quick_edit_mode(options)
{
    options = $.extend({
        mode:  true
        }, options || {});
    if($('#dialog').length != 0)
    {
        options.mode = true;
    }
    quick_edit_mode = options.mode;
}
function django_inline()
{
//    django_inline_toggle();
    $(document).keypress(function(e)
    {
    	if(e.ctrlKey && e.which==13)
    	{
    	   activate_quick_edit();
    	}
    });
}