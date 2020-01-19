# Reactive and complex rendering in the browser

[slides](https://slidr.io/oleksmarkh/reactive-and-complex-rendering-in-the-browser),
[video](https://youtu.be/2IJpcxi7Eto?t=863) (Cogniance Tech Talks Live)

## whoami

[@oleksmarkh](https://twitter.com/oleksmarkh)

## overview

**Leveraging and surpassing DOM (going WebGL), constructing animated scenes.**

(following an issue template)

* motivation <- starting with "why?"
* considerations
* acceptance criteria <- to have an illustrated overview
* steps:
  * use cases for visual programming
  * DOM and beyond: limitations, history, alternatives, standards
  * main players, design, APIs
  * demos
* @see: resources, tools

## what does "reactive" mean?

"a declarative programming paradigm concerned with data streams and the propagation of change. With this paradigm it is possible to express static (e.g., arrays) or dynamic (e.g., event emitters) data streams with ease, and also communicate that an inferred dependency within the associated execution model exists, which facilitates the automatic propagation of the changed data flow."

(https://twitter.com/_ericelliott/status/696321321207271424),
(René Descartes portrait)

## whereis

(use cases)

* animation-heavy interfaces, where huge DOM is too expensive
* data visualization (a new specialization appeared recently - creative coders, data/generative artists)
* maps
  * dominating in geometry calculations
  * raster/vector tiles, layers
* players/editors
  * images (flesh colors, multiplied colors, transparency)
    * organizing metadata
    * preloading (4-pixel thumbnails)
    * cropping, streamlining the layout
  * media controls: audio, video
  * text with effects (typing, fonts, positioning, sizing, colors, etc.) <- [Blotter](https://blotter.js.org)
  * slideshow (combined content, multiple transitions)

## how to leave without the DOM?!

* no layering/cascading
* no event listeners
* no native usual styling

## failed/aged attempts

(https://en.wikipedia.org/wiki/Masyanya#/media/File:Masyanya-Lokhmaty-Hryundel_from_cartoon_Russian_Punk_Rock.gif),
(https://blogs.windows.com/msedgedev/2015/07/02/moving-to-html5-premium-media)

* Flash, Silverlight
* HTML5 features and WebGL instead

## abstractions

* application structure
  * render engine (render loop), world
  * scene, camera (vs. point of view)
  * navigation, interactions
  * helpers (stats: FPS/memory, visual debug)
* own/custom + libs/frameworks
  * d3 utils: [`d3-scale`](https://github.com/d3/d3-scale), [`d3-scale-chromatic`](https://github.com/d3/d3-scale-chromatic), [`d3-color`](https://github.com/d3/d3-color)
  * [`three.js`](https://threejs.org/docs) - a monolithic abstraction over WebGL with fallbacks and helpers
* alternative approaches, APIs:
  * [`regl`](https://github.com/regl-project/regl) - functional WebGL
  * [WebGL for Elm](https://github.com/elm-community/webgl) <- get back later when defining WebGL terms (really nice pipeline diagram)

## shortcuts and risks related to external modules (keeping healthy relationship with OSS)

* being comfortable on the "generic <-> specific" scale
* consistency (semantics/naming, configuration)
* maintenance burden
* contributing back (or riding aside of the road)
* licensing

## low-level APIs (WebGL, Shader Language)

* terms: shader (vertex, fragment), texture, attribute, uniform, etc.
* coords, colors, shapes construction (made of triangles): lines
* passing additional data: abusing textures (sprites and atlases, e.g: patterns in lines, offsets represented as pixel colors)

(reference "WebGL Fundamentals")

## OOP (state management, communication) + FP (state propagation, utils)

Controllable (isolated) state and data pipelines.

(https://twitter.com/mfeathers/status/29581296216)

* towards the reactive paradigm: observing, scheduling, queuing
* tooling: [MobX](https://mobx.js.org/intro/concepts.html), [RxJS](http://reactivex.io/intro.html)

## data processing (cleaning, calculations, conversions), ETL pattern

(example: https://github.com/oleksmarkh/music-stats)

## UI management (fancy term: orchestration)

* components (as a common way these days)
* layering, grouping, accessing (selecting, picking)

## styling

* approaches
  * CSS-like, style as a function of state (e.g. [`styled-components`](https://www.styled-components.com), [`styled-system`](https://github.com/jxnblk/styled-system), [`emotion`](https://emotion.sh/docs/introduction))
  * custom "standards" (declarative DSL for creative development)
  * supporting an ability to use functions and access some granular state
* high-level styling patterns
  * theming (tools and examples: [`styled-tools`](https://github.com/diegohaz/styled-tools), [`typography.js`](https://kyleamathews.github.io/typography.js))
  * responsiveness (restrictions) <- JS constraints vs. CSS media queries (no callbacks)
* testing, reasoning
  * is it possible to assert against layout (other than screenshot comparison)?
  * checking accessibility/usability <- [The Cassius Project](https://cassius.uwplse.org)

## performance (chasing 60 FPS, trying not to drain the battery)

* capabilities of modern browsers
* offloading the main thread (workers and related hassle: passing structured clones)
* DOM: avoiding repaints and reflows ([1](https://developers.google.com/speed/docs/insights/browser-reflow), [2](https://gist.github.com/paulirish/5d52fb081b3570c81e3a))
* pre-rendering, pre-cooking the data <- e.g. tiling
* lazy calculations, limited to viewport
* start/stopping the render loop (`cancelAnimationFrame()`)
* benchmarking

## recommended resources (docs, articles, videos)

### styling

* ["Component Based Design System With Styled-System"](https://varun.ca/styled-system) by Varun Vachhar, 2018

### front-end tooling

* ["React and D3, Together"](https://www.youtube.com/watch?v=SVbTTUpCLfo) by Shirley Xueyang Wu at [ReactiveConf 2017](https://reactiveconf.com/videos)

### dealing with pictures

* ["Building the Google Photos Web UI"](https://medium.com/google-design/google-photos-45b714dfbed1) by Antin Harasymiv, 2018 <- and comments!

### graphics pipeline

* ["A trip through the Graphics Pipeline 2011"](https://fgiesen.wordpress.com/2011/07/09/a-trip-through-the-graphics-pipeline-2011-index) by Fabian Giesen, 2011
* ["Introduction to compute shaders"](https://anteru.net/blog/2018/intro-to-compute-shaders) by Anteru, 2018

### WebGL

* ["WebGL Fundamentals"](https://webglfundamentals.org/webgl/lessons/webgl-fundamentals.html)
* ["Drawing Lines is Hard"](https://mattdesl.svbtle.com/drawing-lines-is-hard) by Matt DesLauriers, 2015 <- show the ["Triangulated Lines" demo](https://mattdesl.svbtle.com/drawing-lines-is-hard#triangulated-lines_1)
* ["Shader-Based Antialiased Dashed Stroked Polylines"](http://jcgt.org/published/0002/02/08) by Nicolas Rougier, 2013 <- take 1-2 figures as examples
* ["How I built a wind map with WebGL"](https://blog.mapbox.com/how-i-built-a-wind-map-with-webgl-b63022b5537f) by Vladimir Agafonkin, 2017
* ["GPU text rendering with vector textures"](https://wdobbie.com/post/gpu-text-rendering-with-vector-textures) by Sydneysider, 2016
* ["Rendering Text with WebGL"](https://unsoundscapes.com/slides/2018-07-05-rendering-text-with-webgl) by Andrey Kuzmin at [Elm Europe 2018](https://2018.elmeurope.org)

## demo, live coding

(20-30 min)

### playground: notebooks - white pater, story, documentation + live code examples

* come from Python (Jupiter), lately adopted by ML community
* [Observable](https://beta.observablehq.com/collection/webgl) <- attractor as an example

### gravitating thumbnails

* showcase
* describe relation between DOM events and three.js code
  * resizing
  * updating debugging helpers
* debugging flags
* cumbersome pieces:
  * ["Splitting sprites (texture atlases) into tiles"](https://stackoverflow.com/questions/47593597/splitting-sprites-texture-atlases-into-tiles-with-three-js)
  * ["Keeping FPS in a certain range"](https://stackoverflow.com/questions/47681058/keeping-fps-in-a-certain-range-with-three-js)

## final thoughts

* performance
  * benchmark from the very beginning
  * profile on multiple configurations
* docs
  * sometimes, docs are awful, incomplete, boring or entirely missing
  * encourage to document findings (contribute to official docs, keep tutorials updated, ask and answer SO questions)
