// All logic now in stores/user.js


// import axios from "axios";
// // import Cookies from 'js-cookie'
//
// // export function login(username, password) {
// //     return axios.post("http://127.0.0.1:8000/api/users/login/", {}, {
// //         auth: {
// //             username,
// //             password
// //         }
// //     }).then(res => {
// //         return res.data
// //     })
// // }
//
// // export async function getUser() {
// //     const csrfToken = Cookies.get('csrftoken');
// //
// //     const response = await axios.post(
// //         "http://127.0.0.1:8000/api/users/active/?format=json",
// //         {},
// //         {headers: {'X-CSRFToken': csrfToken}}
// //     )
// //     return response.data
// // }
//
// export async function getUser(authToken) {
//     const response = await axios.post(
//         "http://127.0.0.1:8000/auth/user/",
//         {},
//         {
//             headers: {'Authorization': 'Token ' + authToken},
//         }
//     )
//     return response.data
// }
//
// export async function login(username, password) {
//     const response = await axios.post(
//         "http://127.0.0.1:8000/auth/login/",
//         {
//             username,
//             password
//         }
//     )
//     return response.data
// }
//
// export async function logout() {
//     const response = await axios.post(
//         "http://127.0.0.1:8000/auth/logout/",
//         {}
//     )
//     return response.data
// }
