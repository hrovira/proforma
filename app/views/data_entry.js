var Template = require("../templates/data_entry");

module.exports = Backbone.View.extend({
    initialize: function(options) {
        console.log("data_entry");

        _.bindAll(this, "bindData");

        var bindFn = _.after(2, this.bindData);
        this.model.on("load", bindFn);
        this.options.questionaire.on("load", bindFn)
    },

    bindData: function() {
        _.each(this.options.questionaire.get("sections"), function(section) {
            _.each(section.questions, function(question) {
                question.isText = _.isEqual(question.dataType, "text");
                question.isDate = _.isEqual(question.dataType, "date");
                question.isRadio = _.isEqual(question.dataType, "radio");
            });
        });

        this.$el.html(Template({ "sections": this.options.questionaire.get("sections") }));
    }
});