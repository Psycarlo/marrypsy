import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import { auth } from "../firebase";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/eighteen",
    name: "Eighteen",
    component: () =>
      import(/* webpackChunkName: "eighteen" */ "../views/Eighteen.vue")
  },
  {
    path: "/register",
    name: "Register",
    component: () =>
      import(/* webpackChunkName: "register" */ "../views/Register.vue")
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Login.vue")
  },
  {
    path: "/interest",
    name: "Interest",
    component: () =>
      import(/* webpackChunkName: "interest" */ "../views/Interest.vue"),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/main",
    name: "Main",
    component: () => import(/* webpackChunkName: "main" */ "../views/Main.vue"),
    meta: {
      requiresAuth: true
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

let redirectMainCounter = 0;

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(x => x.meta.requiresAuth);

  if (requiresAuth && !auth.currentUser) {
    next("/login");
  } else {
    console.log(from.name);
    if ((!from.name || from.name === "Home") && redirectMainCounter === 0) {
      redirectMainCounter++;
      next("/main");
      redirectMainCounter = 0;
    }
    next();
  }
});

export default router;
