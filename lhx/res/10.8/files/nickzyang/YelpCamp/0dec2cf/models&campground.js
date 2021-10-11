var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var campgroundSchema = new Schema({
    name: String,
    price: String,
    img: String,
    description: String,
    author: {
        id: {
            type: Schema.Types.ObjectId,
            ref: 'User'
        },
        username: String
    },
    comments: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'Comment'
        }
    ]
});

module.exports = mongoose.model("Campground", campgroundSchema);
