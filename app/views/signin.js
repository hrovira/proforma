var Template = require("../templates/signin");

module.exports = Backbone.View.extend({
    events: {

    },

    initialize: function(options) {
    },

    render: function() {
        this.$el.html(Template({}));
        return this;
    }
});