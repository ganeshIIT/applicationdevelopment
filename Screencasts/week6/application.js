const About = Vue.component('about', {
    template: `
    <div>
      <h3> About </h3>
          <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.<p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque accumsan, tortor eu fringilla hendrerit, nunc metus luctus massa, sit amet aliquam magna dolor ac magna. Integer nec quam feugiat, viverra eros id, tincidunt arcu. Nullam ipsum purus, suscipit ac neque sed, lacinia maximus nibh. Pellentesque tortor mauris, sagittis non suscipit quis, consequat posuere ante. Morbi eget sagittis mauris. Nam quis facilisis leo. Nullam at nunc ut urna scelerisque semper ac tincidunt libero. Donec eget purus at metus tempus tincidunt eu sed erat. Phasellus at scelerisque sapien. Aenean nulla mi, vestibulum id iaculis sit amet, laoreet eget ipsum.<p>
        <p>Vestibulum venenatis placerat quam eu pharetra. Ut a mi imperdiet, efficitur nunc sed, fringilla est. Phasellus id felis eget leo vulputate bibendum sit amet nec lorem. Nam et ligula lorem. Nullam lobortis condimentum lacus, et ultricies nisl interdum vitae. Aenean euismod, erat ac vestibulum fermentum, erat eros dapibus ligula, a dignissim lorem tellus vel purus. Ut cursus quis mauris non pharetra.</p>
    </div>`
})

const PrivacyPolicy = Vue.component('privacy-policy', {
    template: `
    <div>
      <h3> Privacy Policy </h3>
          <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.<p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque accumsan, tortor eu fringilla hendrerit, nunc metus luctus massa, sit amet aliquam magna dolor ac magna. Integer nec quam feugiat, viverra eros id, tincidunt arcu. Nullam ipsum purus, suscipit ac neque sed, lacinia maximus nibh. Pellentesque tortor mauris, sagittis non suscipit quis, consequat posuere ante. Morbi eget sagittis mauris. Nam quis facilisis leo. Nullam at nunc ut urna scelerisque semper ac tincidunt libero. Donec eget purus at metus tempus tincidunt eu sed erat. Phasellus at scelerisque sapien. Aenean nulla mi, vestibulum id iaculis sit amet, laoreet eget ipsum.<p>
        <p>Vestibulum venenatis placerat quam eu pharetra. Ut a mi imperdiet, efficitur nunc sed, fringilla est. Phasellus id felis eget leo vulputate bibendum sit amet nec lorem. Nam et ligula lorem. Nullam lobortis condimentum lacus, et ultricies nisl interdum vitae. Aenean euismod, erat ac vestibulum fermentum, erat eros dapibus ligula, a dignissim lorem tellus vel purus. Ut cursus quis mauris non pharetra.</p>
    </div>`
})

const MessageBoard = Vue.component('message-board', {
    props: ["title"],
    template: `
    <div>
      <h3> {{ title }} </h3>
          <div class="form-group">
            <label for="vistor_name">Your Name</label>
            <input type="text" id="vistor_name" v-model="vistor_name" /> 
          </div>
          <div class="form-group">
            <label for="vistor_message">Your Message</label>
            <input type="text" id="vistor_message" v-model="vistor_message" /> 
          </div>
          <button v-on:click="sayHi">Say Hi</button>
          <i class="bi bi-cloud-arrow-up-fill"  v-bind:class="savedIconClass"></i>

        <h3> Messages </h3>
        <ul>
            <li v-for="message in messages"> {{message['vistor_name']}} - {{message['vistor_message']}}</li>
        </ul>
    </div>
        `,
    data: function() {
        return {
            vistor_name: null,
            vistor_message: null,
            messages: [],
            savedIconClass: "text-success" // text-danger text-warning
        }
    },
    methods: {
        sayHi: function(name) {
            this.messages.push({
                "vistor_name": this.vistor_name,
                "vistor_message": this.vistor_message
            });
            this.savedIconClass = "text-warning";
            fetch('https://httpbin.org/post', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        "for": this.title,
                        "vistor_name": this.vistor_name,
                        "vistor_message": this.vistor_message
                    }),
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                    this.savedIconClass = "text-success";
                })
                .catch((error) => {
                    console.error('Error:', error);
                    this.savedIconClass = "text-danger";
                });

            this.vistor_name = "";
            this.vistor_message = "";
            this.$emit('add-to-grand-total');


        }
    },
    computed: {
        count: function() {
            return this.messages.length;
        }
    },

    mounted: async function() {
        r = await fetch("example-response.json")
        d = await r.json()
        console.log(d)
        this.messages = [{
            "for": "fatima",
            "vistor_name": "Rajesh",
            "vistor_message": "Hello world"
        }]
    }
})

const NotFound = { template: '<p>Page not found</p>' }

const routes = [{
    path: '/',
    component: MessageBoard,
    props: { title: 'Fatima' }
}, {
    path: '/about',
    component: About
}, {
    path: '/privacy-policy',
    component: PrivacyPolicy
}];

const router = new VueRouter({
  routes // short for `routes: routes`
})


var app = new Vue({
    el: '#app',
    router: router,
    data: {
        grand_total: 0
    },
    methods: {
        add_grand_total: function() {
            console.log("in grand_total");
            this.grand_total = this.grand_total + 1;
        }
    }

})