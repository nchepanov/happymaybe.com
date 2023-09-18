[![Netlify Status](https://api.netlify.com/api/v1/badges/0fb35d62-0ede-4117-b704-39c747ae2088/deploy-status)](https://app.netlify.com/sites/happymaybe/deploys)

# Happy Maybe Podcast   

## Stack

* Web analytics via Plausible https://plausible.io/happymaybe.com
  * credentials owned by Nikita
  * $9/mo paid by Nikita since it's also used for chepanov.com
* Podcast mp3 hosting via AWS S3 https://happymaybe.s3.amazonaws.com
  * credentials owned by Vasily
  * cost is $1/mo
* Website hosting via Netlify https://app.netlify.com/sites/happymaybe
  * credentials owned by Nikita
  * free
* Podcast feed hosted via Indeedcast https://www.indeecast.com/api/v2/podcast/published/1403141
  * credentials owned by Vasily
  * free

## Runbooks

### Adding an episode

* Confirm the new mp3 is available in AWS S3 bucket
* Ensure indeecast.com [feed](https://www.indeecast.com/p/happy-maybe/feed) was updated with the new episode
* Run `curl https://www.indeecast.com/p/happy-maybe/feed > happiness-not-guaranteed.xml`
* Then run `./script/generate.py happiness-not-guaranteed.xml`
* Test with `hugo serve`
* If everything looks correct locally, run `git add . && git commit -am "Add new episode" && git push origin main`

### Making changes to the site

- Clone the repo
- Install `brew install hugo`
- Start the Hugo sever `hugo serve`

> Alternatively, you can run this locally with [the Netlify CLI](https://docs.netlify.com/cli/get-started/)'s by running the `netlify dev` command for more options like receiving a live preview to share (`netlify dev --live`) and the ability to test [Netlify Functions](https://www.netlify.com/products/functions) and [redirects](https://docs.netlify.com/routing/redirects/). 

Netlify is [setup](https://app.netlify.com/sites/happymaybe/deploys) to automatically deploy on push. For fine grained control, you can:

- Install the Netlify CLI globally `npm install netlify-cli -g`
- Then use the `netlify deploy` for a deploy preview link or `netlify deploy --prod` to deploy to production
