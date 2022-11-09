var app = new Vue({
  el: '#app',
  data: {
    vistor_name: null,
    vistor_message : null,
    messages: []
  },
  methods: {
    sayHi: function (name) {
      this.messages.push({"vistor_name":this.vistor_name, "vistor_message":this.vistor_message});
      this.vistor_name = "";
      this.vistor_message = "";
    }
  },
  computed : {
      count: function(){
          return this.messages.length;
      }
  }    
})
