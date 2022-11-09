var app = new Vue({
    el: "#app",
    
    data: {
        message: "Hello world",
        visitor_name: "",
        visitors: []
    },

    methods: {
        sayHi: function(){
            this.message = "Hi",
            // this.count++,
            this.visitors.push(this.visitor_name),
            this.visitor_name =""
        }
    },

    computed: {
        count: function(){
            return this.visitors.length;
        }
    }
})