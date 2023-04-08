[![Netlify Status](https://api.netlify.com/api/v1/badges/0fb35d62-0ede-4117-b704-39c747ae2088/deploy-status)](https://app.netlify.com/sites/happy-maybe/deploys)

# Happy Maybe podcast   

## Quick setup

 ### 1. Cloning + Running Locally

 - Clone this repo with one of these options:
 - Start the Hugo sever `hugo server -D`

  > Alternatively, you can run this locally with [the Netlify CLI](https://docs.netlify.com/cli/get-started/)'s by running the `netlify dev` command for more options like receiving a live preview to share (`netlify dev --live`) and the ability to test [Netlify Functions](https://www.netlify.com/products/functions) and [redirects](https://docs.netlify.com/routing/redirects/). 

### 2. Deploying
 - Install the Netlify CLI globally `npm install netlify-cli -g`
    
 - Run `hugo`

 - Then use the `netlify deploy` for a deploy preview link or `netlify deploy --prod` to deploy to production


## Adding an episode

> THIS IS A WORK IN PROGRESS

* Use `git lfs` to upload new episode
* Run a script to regenerate `posts/` based on the podcast XML
* `git commit -am "New episode" && git push origin main`

## Testing

### Included Default Testing

We’ve included some tooling that helps us maintain these templates. This template currently uses:

- [Renovate](https://www.mend.io/free-developer-tools/renovate/) - to regularly update our dependencies
- [Cypress Netlify Build Plugin](https://github.com/cypress-io/netlify-plugin-cypress) - to run our tests during our build process

If your team is not interested in this tooling, you can remove them with ease!

### Removing Renovate

In order to keep our project up-to-date with dependencies we use a tool called [Renovate](https://github.com/marketplace/renovate). If you’re not interested in this tooling, delete the `renovate.json` file and commit that onto your main branch.
