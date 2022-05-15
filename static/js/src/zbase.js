export class AcGame {
    constructor(id) {
        this.id = id;
        this.$ac_game = $('#' + id);
        this.settings = new Settings(this); // 创建Settings模块，这个一定要放在Menu之前。
        this.menu = new AcGameMenu(this);
        // console.log("test");
        // this.playground = new AcGamePlayground(this);

        this.start();
    }

    start() {
    }
}