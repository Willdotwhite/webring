# Will's Simple Webring

This webring isn't really a webring.

I'm so good at naming things.

This is a static JSON file accessible here: https://willdotwhite.github.io/webring/data.json

All members of the community can fetch this file on demand and do whatever they like with it - traditional webring, list of people in an &lt;aside>, interactive web game; the sky's the limit!

## Joining the webring

1. Submit a pull request to `data.json` to add yourself to the list
2. Ping me to let me know you've done it
3. Integrate it into your website somehow

### Join Criteria

I know you, or someone I trust vouches for you :D

This is not a public webring (yet) but a webring of friends and the cool stuff they do.

## Adding your site to the code

Fill in your details in the JSON list - the setup is this:

```json
{
  "name": "What name would you like to be referred to",
  "title": "Short title of your site/project",
  "description": "One line sentence that others can use to signpost your site",
  "url": "https://theactuallyonlyimportantthinginthe.list"
}
```

## Adding the webring to your site

The list is shuffled daily, so your integration just needs to pull the JSON data down.

<details>

<summary>Pre-built JS reference function</summary>

```js
/**
 * Get the webring neighbours for your URL!
 * @credit Sophie<sophies.games>
 */
async function get_webring_neighbours(my_url) {
    // Fetch webring json array
    const request = await fetch('https://willdotwhite.github.io/webring/data.json');
    const webring_array = await request.json();

    // URLs are case-insensitive, so checks should be done with both sides of a comparison lowercased
    my_url = my_url.toLowerCase();

    // Find the index of your website in the ring
    const my_index = webring_array.findIndex(obj => obj.url.toLowerCase().includes(my_url));
    if (my_index === -1) {
        throw new Error(`Your URL "${my_url}" was not found in the webring.`)
    }

    // Your left neighbour is the one before you in the list, hence -1
    // Your right neighbour is the one after you in the list, hence +1
    const left_neighbour_index = my_index - 1;
    const right_neighbour_index = my_index + 1;

    // To make the "ring" part of "webring" work we then wrap around to the start/end if either the left/right indicies go out of bounds
    if (left_neighbour_index < 0) left_neighbour_index = webring_array.length - 1;
    if (right_neighbour_index >= webring_array.length) right_neighbour_index = 0;

    // Return a tuple where the first object is the left neighbour, the second object is the right neighbour
    return [
        webring_array[left_neighbour_index],
        webring_array[right_neighbour_index]
    ];
}
```

</details>

## Reference: [ktyl.dev](https://ktyl.dev)

<img width="1250" height="256" alt="image" src="https://github.com/user-attachments/assets/82498c3f-3194-4422-aecb-c7ab316dd4ef" />

<details>

<summary>Pure HTML/CSS rendering (build-time implementation)</summary>

Pure HTML/CSS version is provided first, see note about actual implementation later.

```html
<p class="webring header">
    Part of the <a href="https://willdotwhite.github.io/webring">Unofficial GMTK Webring!</a>
</p>

<!-- Pick the links out of https://willdotwhite.github.io/webring/data.json -->
<p class="webring links">
    <a href="https://badlydone.dev">← https://badlydone.dev</a>
    <span class="webring splitter"></span>
    <a href="https://kevinvognar.com">https://kevinvognar.com →</a>
</p>
```

```css
:root {
    --color-text: #444;
    --color-accent: #ff369a;
}

.webring {
    text-align: center;
}

.webring.header {
    margin-top: 50px;
}

.webring.links {
    margin-bottom: 50px;
}

.webring.splitter {
    width: 40px;
    height: 4px;
    margin: 0 10px 3px 10px;
    background-color: var(--color-accent);
    display: inline-block;
}

a {
    text-decoration: underline 2px var(--color-accent);
    padding: 0 2px;
    color: var(--color-text);
}

a:hover {
    text-decoration: none;
    border: solid 2px var(--color-accent);
    border-radius: 4px;
    box-sizing: border-box;
    padding: 0;
}

a:visited {
    color: var(--color-accent);
}
```

The above should be enough to implement the component accurately with no dependencies, however in practice it is implemented using the [Astro](https://astro.build/) framework, which allows for scripting to run at build-time to dynamically determine the links. The Astro component can be found verbatim [here](https://sauce.wednesday.pizza/ktyl/ktyl.dev/src/components/Webring.astro), which includes some templating and JavaScript to do aforementioned generation.

</details>
