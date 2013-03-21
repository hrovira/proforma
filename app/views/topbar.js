var Template = require("../templates/topbar");

module.exports = Backbone.View.extend({

    render: function() {
        this.$el.html(Template({
            "whoami": this.options.whoami,
            "loggedin": !_.isEmpty(this.options.whoami)
        }));
        return this;
    }
});