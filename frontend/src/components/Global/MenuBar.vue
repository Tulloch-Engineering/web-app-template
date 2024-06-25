<template>
  <div ref="expandedSidebar">
    <div class="top-box">
      <div class="first-box">
        <div class="menu-btn" v-on:click="sidebarStatus = !sidebarStatus">
          menu
        </div>
        <img
          id="tulloch-img"
          src="@/assets/images/tulloch-logo.png"
          @click="this.$router.push('/')"
        />
        <h1 class="title">{{ Title }}</h1>
      </div>
    </div>
    <div class="bottom-box"></div>
    <transition name="popup">
      <div class="popup" v-if="sidebarStatus">
        <div
          style="
            position: absolute;
            right: 0;
            font-family: 'MaterialSymbolsRounded';
            font-size: 1.8rem;
            color: #323982;
            cursor: pointer;
            width: fit-content;
            margin: 5px;
            right: 20px;
          "
          v-on:click="sidebarStatus = !sidebarStatus"
        >
          close
        </div>
        <img id="tulloch-img" src="@/assets/images/tulloch-logo.png" alt="" />
        <div class="side-item" @click="this.$router.push('/')">Open Tender</div>
        <div class="side-item" @click="this.$router.push('/OtherPage')">
          Active Bid
        </div>
        <div class="side-item" @click="this.$router.push('/OtherPage')">Accepted</div>
        <div class="side-item" @click="this.$router.push('/OtherPage')">Closed</div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  // props: {
  // },
  data() {
    return {
      sidebarStatus: false,
      Title: 'List of Tenders',
    }
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside)
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside)
  },
  methods: {
    handleClickOutside(event) {
      if (!this.$refs.expandedSidebar.contains(event.target)) {
        this.sidebarStatus = false
      }
    },
  },
}
</script>

<style scoped>
.popup {
  background-color: #a4a3c4;
  top: 0;
  left: 0;
  position: absolute;
  height: 99%;
  width: 18vw;
  min-width: 250px;
  max-width: 600px;
  border: 4px solid #323982;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  display: flex row;
}

.popup.show {
  transform: translateX(0);
}

.side-item {
  border: 2px solid #323982;
  font-size: 1.5rem;
  padding-left: 8px;
  color: #323982;
  font-family: 'Helvetica-bold';
  cursor: pointer;
  transition: 0.5s border-color;
  padding: 6px;
}

.side-item:hover {
  border-color: #75b643;
}

.top-box {
  height: 3rem;
  width: 100%;
  background-color: #a4a3c5;
  display: flex;
  align-items: center;
}

.first-box {
  flex: 1 1 auto;
  display: flex;
  align-items: center;
}

.menu-btn {
  font-family: 'MaterialSymbolsRounded';
  height: 1em;
  width: 1em;
  flex: 0 1 auto;
  display: flex;
  font-weight: bold;
  justify-content: flex-end;
  align-items: center;
  transition: color 0.5s; /* Add this line to set the transition */
  color: #323982;
  cursor: pointer;
  margin: 10px;
}

#tulloch-img {
  width: 10vw;
  height: auto;
  margin: 0.5rem;
  cursor: pointer;
}

.title {
  color: #323982;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  white-space: nowrap;
  font-size: calc(4vw);
}

@media (min-width: 840px) {
  /* If minimum width is 999px then act as follow: Used for desktop */
  #tulloch-img {
    width: 5rem;
    margin: 0.5rem;
  }

  .title {
    font-size: 2rem;
  }

  .menu-btn {
    font-size: 2.2rem;
  }
}

.bottom-box {
  height: 0.25rem;
  background-color: #323982;
}

.menu-btn:hover {
  color: #75b643;
}
</style>
