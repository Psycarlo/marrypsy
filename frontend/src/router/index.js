import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import { auth } from "../firebase";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      authRedirectToMain: true
    }
  },
  {
    path: "/eighteen",
    name: "Eighteen",
    component: () =>
      import(/* webpackChunkName: "eighteen" */ "../views/Eighteen.vue"),
    meta: {
      authRedirectToMain: true
    }
  },
  {
    path: "/register",
    name: "Register",
    component: () =>
      import(/* webpackChunkName: "register" */ "../views/Register.vue"),
    meta: {
      authRedirectToMain: true
    }
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Login.vue"),
    meta: {
      authRedirectToMain: true
    }
  },
  {
    path: "/interest",
    name: "Interest",
    component: () =>
      import(/* webpackChunkName: "interest" */ "../views/Interest.vue"),
    meta: {
      requiresAuth: true,
      authRedirectToMain: true
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

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(x => x.meta.requiresAuth);
  const authRedirectToMain = to.matched.some(x => x.meta.authRedirectToMain);
  // TODO: Refactor - When register -> Interest
  if (auth.currentUser && authRedirectToMain) {
    next("/main");
  }
  if (requiresAuth && !auth.currentUser) {
    next("/login");
  }
  next();
});

export default router;
