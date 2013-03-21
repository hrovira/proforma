var Template = require("../templates/grid");

module.exports = Backbone.View.extend({
    initialize: function(options) {
        _.bindAll(this, "bindData");

        this.model.on("load", this.bindData);
    },

    render: function() {
        this.$el.html(Template({"title": this.options.title }));
        return this;
    },

    bindData: function() {
        var items = this.model.get("items");
        var headers = _.without(_.keys(items[0]), "uri", "id");
        var rows = _.map(items, function (item) {
            return { "values":_.map(headers, function (header) {
                return item[header];
            })};
        });

        this.$el.html(Template({ "title": this.options.title, "headers":headers, "rows":rows }));
    }
});