const fetch = require('node-fetch');


//***************************************************//

// let username = 'saintaubins'

// async function getEvents(username) {
//     const events = []
//     let page = 1
  
//     do {
//       const url = `https://api.github.com/users/${username}/events?page=${page}`
//       var body = await fetch(url).then(res => res.json())
//       page++
//       events.push(...body)
//     } while(!body.length)
  
//     return events
//   }
  
//   (async () => {
//     const events = await getEvents('handtrix')
  
//     console.log('Overall Events', events.length)
//     console.log('PullRequests', events.filter(event => event.type === 'PullRequestEvent').length)
//     console.log('Forks', events.filter(event => event.type === 'ForkEvent').length)
//     console.log('Issues', events.filter(event => event.type === 'IssuesEvent').length)
//     console.log('Reviews', events.filter(event => event.type === 'PullRequestReviewEvent').length)
//   })()

// let url = `https://api.github.com/users/${username}/`

// let response = fetch(url).then(response => {
//     console.log(response)
//     console.log('hello1')
// })

// fetch(url).then(response => {
//     console.log(response)
//     console.log('hello2')
// })

//console.log('hello')

//fetch('http://reqres.in/api/users')

//******************************************************************* //

async function getContributions(token, username) {
  const headers = {
      'Authorization': `bearer ${token}`,
  }
  const body = {
      "query": `query {
          user(login: "${username}") {
            name
            contributionsCollection {
              contributionCalendar {
                colors
                totalContributions
                weeks {
                  contributionDays {
                    color
                    contributionCount
                    date
                    weekday
                  }
                  firstDay
                }
              }
            }
          }
        }`
  }
  const response = await fetch('https://api.github.com/graphql', { method: 'POST', body: JSON.stringify(body), headers: headers })
  const data = await response.json()
  return data
}

//const data = getContributions('token', 'saintaubins')
//console.log(data)