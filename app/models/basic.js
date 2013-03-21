module.exports = Backbone.Model.extend({
    url: function() {
        return this.get("url");
    },

    fetch:function (options) {
        var _this = this;
        return Backbone.Model.prototype.fetch.call(this, _.extend({
            success: function() {
                _this.trigger("load");
            }
        }, options));
    }
});