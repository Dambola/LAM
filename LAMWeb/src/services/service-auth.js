import axios from 'axios';

class AuthService {
  login(username, password) {
    return axios.post('http://localhost:8081/auth', {
        'login': username,
        'password': password
      }).then(response => {
        if (response.data.accessToken) {
          axios.defaults.headers.common['Authorization'] = response.data.accessToken;
          localStorage.setItem('user', JSON.stringify(response.data));
          return true;
        }
      });
      return false;
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.put('auth', {
      username: user.username,
      email: user.email,
      password: user.password
    });
  }
}

export default new AuthService();