Vue.component('tic', {
    props: ['pos'],
    template: `<span v-html="imgl" v-on:click="setVal(pos);"></span>`,
    methods: {
        setVal() {
            this.$parent.setVal(this.pos);
        }
    },
    computed: {
        imgl: function() {
            return `<img src="assets/${this.$parent.v2c(this.$parent.board[this.pos])}.png" />`;
        }
    }
})

var app = new Vue({
    el: '#app',
    data: {
        board: [0, 0, 0, 0, 0, 0, 0, 0, 0],
        next: 1,
    },
    methods: {
        v2c(r) {
            return (r == 1) ? 'x' : (r == -1) ? 'o' : 'b';
        },
        setVal(i) {
            if (this.result == 0) {
                if (this.board[i] == 0) {
                    Vue.set(this.board, i, this.next);
                    this.next = -this.next;
                }
            }
        },
    },
    computed: {
        headmsg: function() {
            let msg = "";
            switch(this.result) {
                case 0: msg = `<h1>Next move: <img src="assets/${this.v2c(this.next)}.png" /></h1>`; break;
                case 1: msg = `<h1>Congratulations <img src="assets/x.png" />`; break;
                case -1: msg = `<h1>Congratulations <img src="assets/o.png" />`; break;
                case 2: msg = `<h1>Boring draw!</h1>`; break;
                default: msg = "Hello?"; break;
            }
            return msg;
        },
        result: function() {
            let patts = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]];
            for (p of patts) {
                const sum = p.reduce((a, i) => a + this.board[i], 0);
                if (sum == 3) {
                    return 1;   // X won
                } else if (sum == -3) {
                    return -1;  // O won
                }
            }
            for (i in this.board) {
                if (this.board[i] == 0) return 0;    // Still in progress
            }
            return 2;   // Draw
        }
    }
})
