//standard ally script
window.ALLY_CFG = {
    'baseUrl': 'https://prod.ally.ac',
    'clientId': 5145,
    'lti13Id': '134300000000000195'
};
$.getScript(ALLY_CFG.baseUrl + '/integration/canvas/ally.js');


////////////////////////////////////////////////////
// DESIGN TOOLS CONFIG                            //
////////////////////////////////////////////////////
// Copyright (C) 2017  Utah State University
var DT_variables = {
        iframeID: '',
        // Path to the hosted USU Design Tools
        path: 'https://designtools.ciditools.com/',
        templateCourse: '130252',
        // OPTIONAL: Button will be hidden from view until launched using shortcut keys
        hideButton: true,
    	 // OPTIONAL: Limit by course format
	     limitByFormat: false, // Change to true to limit by format
	     // adjust the formats as needed. Format must be set for the course and in this array for tools to load
	     formatArray: [
            'online',
            'on-campus',
            'blended'
        ],
        // OPTIONAL: Limit tools loading by users role
        limitByRole: true, // set to true to limit to roles in the roleArray
        // adjust roles as needed
        roleArray: [
            'admin',
            'teacher'      
        ],
        // OPTIONAL: Limit tools to an array of Canvas user IDs
        limitByUser: false, // Change to true to limit by user
        // add users to array (Canvas user ID not SIS user ID)
        userArray: [
            '1234',
            '987654'
        ],
		 // OPTIONAL: Relocate Ally alternative formats dropdown and hide heading
		 overrideAllyHeadings: false,
		 // OPTIONAL: Make assignment rubrics sortable
		 sortableRubrics: false,
		 // OPTIONAL: Transform people page ina course to show student cards
		 showStudentCards: false
};

// Run the necessary code when a page loads
$(document).ready(function () {
    'use strict';
    // This runs code that looks at each page and determines what controls to create
    $.getScript(DT_variables.path + 'js/master_controls.js', function () {
        console.log('master_controls.js loaded');
    });
});
////////////////////////////////////////////////////
// END DESIGN TOOLS CONFIG                        //
////////////////////////////////////////////////////

//nickelled script
$(document).ready(function(){console.log("document.ready");
window.NickelledSettings = {
	userId: ENV.current_user.id
  };

  var NickelledLaunchers = window.NickelledLaunchers = NickelledLaunchers||{};

 NickelledLaunchers.preloadEvents = [];
 

 NickelledLaunchers.show = function() {NickelledLaunchers.preloadEvents.push('show') };
 
 NickelledLaunchers.hide = function(){NickelledLaunchers.preloadEvents.push('hide') };
 
 
 if (ENV.current_user_roles.indexOf("teacher")!==-1){
 
 NickelledLaunchers.show();
 
 jQuery.getScript('https://cdn.nickelled.com/launchers.min.js') ;
 }
 
 })
 
 
//hide course reset button
$(document).ready(function(){
if($.inArray('admin',ENV['current_user_roles']) == -1) {
$("a.Button.Button--link.Button--link--has-divider.Button--course-settings.reset_course_content_button").hide();
}
})

//hide course reset button
$(document).ready(function(){
if($.inArray('admin',ENV['current_user_roles']) == -19) {
$("a.Button.Button--link.Button--link--has-divider.Button--course-settings.reset_course_content_button").hide();
}
})




// accordion fix
!function(s,d,url,e,p){
  e=d.createElement(s),p=d.getElementsByTagName(s)[0];e.async=1;e.src=url;p.parentNode.insertBefore(e,p)
}('script', document, 'https://unpkg.com/widgetize-canvas-lms-user-content');