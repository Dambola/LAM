import Vue from 'vue'
import { lamapi } from '../boot/axios'
import { uid } from 'quasar'

// The data goes here
const state = {
  musics: {}
};

// Contains not assynchronous -> Change state directly
const mutations = {
  reloadMusics (state, musics) {
    musics.forEach((music) => {
      Vue.set(state.musics, music.id, music);
    });
  },
  
  updateMusic (state, payload) {
    Object.assign(state.musics[payload.id], payload);
  },

  deleteMusic (state, id) { 
    Vue.delete(state.musics, id);
  },

  createMusic (state, payload) {
    Vue.set(state.musics, payload.id, payload.music);
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
  reloadMusics ({ commit }) {
    lamapi.get('music').then(response => {
      if (response.data.musics) {
        commit('reloadMusics', response.data.musics);
      }
    });
  },

  async updateMusic ({ commit }, payload) {
    try {
      const response = await lamapi.post('music', payload);
      commit('updateMusic', payload);

    } catch (error) {
      const { response } = error;
      const { data } = response;
      throw new Error(data.message);
    }
  },

  async deleteMusic ({ commit }, id) {
    try {
      const response = await lamapi.delete('music', { data: { id: id } });
      commit('deleteMusic', id);

    } catch (error) {
      const { response } = error;
      const { data } = response;
      throw new Error(data.message);
    }
  },
  
  async createMusic ({ commit }, payload) {
    try {
      const response = await lamapi.put('music', payload);
      const { data } = response;
      if (data.id) {
        commit('createMusic', { id: data.id, music: payload });
      }

    } catch (error) {
      const { response } = error;
      const { data } = response;
      throw new Error(data.message);
    }      
  }
};

// Get data from a State
const getters = {
  musics: (state) => {
    return state.musics;
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};