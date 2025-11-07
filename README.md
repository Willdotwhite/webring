# Will's Simple Webring

A simple widget that lets you put your site into a linked list of other sites. 

The JS is dirt simple and you can see all it does is some regex on the list of sites and make links.

_Based off [Onionring](https://garlic.garden/onionring)_

_Forked from [randyau/datawebring](https://github.com/randyau/datawebring)

# Joining the webring

1. Submit a pull request to `onionring-variables.js` (details below) to add your site to the list
2. Ping me to let me know you've done it
3. Copy/paste the little HTML code snippet in the Installation section to have the widget show up
4. (Optional) The CSS is super basic. Locally override it to style it for your site.

# Join Criteria

I know you, or someone I trust vouches for you :D

This is not a public webring (yet) but a webring of friends and the cool stuff they do.

# Adding your site to the code

In [`onionring-variables.js`](https://github.com/willdotwhite/webring/blob/main/onionring-variables.js#L9), 
there is a variable `sites` at the top, just add your site to the list. That's it.

Then just submit a Pull Request with your site information. 
If you have trouble or don't know how to do it, please let me know and I'll help.

Once the PR is merged and GitHub Pages builds and updates the CDN, the widget on your site should be able to find its URL and know where it is in the ring.

# Installation of the widget

Place this snippet in your HTML body where you want the widget box to appear.
There's no need to edit or make changes.

The widget requires that your site be on the list of sites (based off URL pattern matching) before it displays correctly. 
Otherwise it displays text saying it hasn't been included in the webring yet.
If your domain or a subdirectory is on the list, the widget should work for any subdirectory under that entry.

```
<div id='a-chill-little-data-ring'>
<script type="text/javascript" src="https://willdotwhite.github.io/webring/onionring-variables.js"></script>
<script type="text/javascript" src="https://willdotwhite.github.io/webring/onionring-widget.js"></script>
</div>
```

## Styling

You may **optionally** put the CSS into your HTML head section to format the widget. It works fine without it.

Add this to the `<head> ... </head>` section for basic styling. Feel free to locally override the settings to suit your own taste.

I haven't edited the CSS yet, so I've no idea what the default looks like!


```
<link rel="stylesheet" href="https://willdotwhite.github.io/webring/onionring.css">
```

# How's it work?

There's a list of sites in `onionring-variables.js`.
When a widget is loaded it looks at the URL of the site it is on and does simple regexp to figure out if it is on the official list of sites.
That lets it know where in the ordered list the browser is currently, and lets users walk the ring using the Next/Previous links. 
If the regex fails to find a match it shows an error message instead. That's it. Simple 90's tech.

## Daily Shuffling

Traditionally, webrings acted like static linked lists where for any given site, the next and previous sites were fixed.
Obviously this creates hotspots where a high traffic site would bias traffic towards its neighbors.
To smooth things out, we've added a PRNG seeded to the date that shuffles the list in a consistent manner. 
That way the hot spots should be smooth over time while still giving visitors a consistent browsing experience that let's them walk the entire ring.

# License

Quoted straight from Onionring's site on 2024-09-20:

_onionring.js and the files that make it up are licensed under the [cooperative non-violent license (CNPL) v7+,](https://thufie.lain.haus/NPL.html) which means, roughly, that anyone is allowed to download, change and share the files as long as you give credit, disclaim what changes you've made, and don't use them to violent, coercive or discriminatory ends._
