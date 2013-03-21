$(function () {
    app = {
        Events: _.extend(Backbone.Events)
    };

    var Model = require("models/basic");

    var Router = require("./router");
    app.Router = new Router();

    $.ajax({
        "url": "auth/whoami",
        "success": function(json) {
            app.Router.allow_in(json);
        },
        "error": function(o) {
            console.log("error=" + o.responseText);
            app.Router.sign_in();
        }
    });

    Backbone.history.start();
    app.Events.trigger("ready");
});
