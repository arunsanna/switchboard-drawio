# Switchboard's draw.io

This fork (branch `switchboard`, based on draw.io v32.4.1) is the editor behind Switchboard
Canvas diagrams. Switchboard turns its changes on with `sb=1` in the editor's address; without
it the editor is unchanged draw.io.

- **Layout (`sb=1`, simple theme):** the drawing fills the page. The toolbar floats as a centred
  bar; the shapes and format panels float over the drawing and start closed; the page tabs
  float at the bottom centre. A click on the empty drawing closes the shapes panel.
  Changes: `grapheditor/Editor.js` (`Editor.switchboard`), `grapheditor/EditorUi.js` (`refresh`),
  `diagramly/EditorUi.js` (closed panels, click to close, no scroll shift),
  `diagramly/Simple.js` (`geSwitchboard` class), `diagramly/Pages.js` (`geGitHubLink`), and the
  Switchboard section at the end of `styles/grapheditor.css`.

## Building

Like upstream, the built bundles are committed. After changing sources under `js/`, rebuild
`js/app.min.js` with draw.io's own build in Docker (no Java on the host):

    docker build -t switchboard-drawio-build etc/switchboard
    docker run --rm -v "$PWD":/drawio switchboard-drawio-build app
    git checkout -- src/main/webapp/js/extensions.min.js src/main/webapp/js/shapes-14-6-5.min.js \
        src/main/webapp/js/viewer.min.js src/main/webapp/js/viewer-static.min.js

The last line keeps bundles the change does not touch as upstream ships them (the build only
reformats them). CSS changes need no build.
