var Model = require("models/basic");
var DataEntryModel = require("models/basic");
var IncompleteEntriesGrid = require("views/grid");
var DataEntryForm = require("views/data_entry");
var SignInView = require("views/signin");

module.exports = Backbone.Router.extend({
    routes: {
        "": "main",
        "home": "main",
        "signin": "sign_in",
        "signout": "sign_out",
        "entries/new": "new_entry",
        "entries/:entry_id": "entry",
        "incomplete": "incomplete"
    },

    main: function() {
        // TODO: Establish a welcome page?
        this.incomplete()
    },

    incomplete: function() {
        var model = new Model({ "url": "dao/entries" });

        var grid = new IncompleteEntriesGrid({ "model": model, "title": "Incomplete Entries" });
        $(".c-main").html(grid.render().el);

        model.fetch({
            "data": {
                "state": "incomplete"
            },
            "traditional": true
        });
    },

    new_entry: function() {
        var model = new DataEntryModel({ });
        var questionaire = new Model({ "url": "data/questionaire.json" });

        var form = new DataEntryForm({ "model": model, "questionaire": questionaire });
        $(".c-main").html(form.render().el);

        questionaire.fetch();
        model.trigger("load");
    },

    entry: function(entryId) {
        var model = new DataEntryModel({ "url": "dao/entries" + (entryId ? "/" + entryId : "") });
        var questionaire = new Model({ "url": "data/questionaire.json" });
        var form = new DataEntryForm({ "model": model, "questionaire": questionaire });
        $(".c-main").html(form.render().el);

        model.fetch();
        questionaire.fetch();
    },

    allow_in: function(json) {
        var TopBar = require("views/topbar");
        var topBar = new TopBar({ "whoami": json });
        $(".c-topbar").html(topBar.render().el);
    },

    sign_in: function() {
        var signIn = new SignInView({});
        $(".c-main").html(signIn.render().el);
    },

    sign_out: function() {
        $.ajax({
            "url": "auth/signout",
            "type": "POST"
        });

        this.navigate("home", {trigger: true});
    }
});
