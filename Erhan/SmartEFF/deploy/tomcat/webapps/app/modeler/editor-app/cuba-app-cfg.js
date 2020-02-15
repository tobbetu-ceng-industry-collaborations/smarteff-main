'use strict';

var CUBA = CUBA || {};

CUBA.CONFIG = {
    modelerRoot: function () {
        var href = window.location.href;
        return href.substring(window.location.origin.length, href.indexOf("/modeler/") + "/modeler/".length);
    }
}