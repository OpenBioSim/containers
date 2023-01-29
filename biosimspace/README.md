# BioSimSpace container

This container provides a base BioSimSpace installation, together with 
ipython, jupyterlab, git, nano, gromacs, ambertools and plumed
(where they are available)

Build a combined x86-64/arm64 image by first starting a buildx builder

```
$ docker buildx create --name mybuilder --driver docker-container --bootstrap
```

Then you need to switch to that builder

```
$ docker buildx use mybuilder
```

Or, if you prefer a single line command

```
$ docker buildx create --name mybuilder --driver docker-container --bootstrap --use
```

And then you can build a combined ARM64/X86-64 container using the command

```
$ docker buildx build --platform linux/amd64,linux/arm64 -t openbiosim/biosimspace:latest . --push
```

NOTE - you need the `--push` as the container must be pushed as soon as it is built.

Finally, you need to tag the image using the version number for sire, e.g.

```
$ docker buildx imagetools create -t openbiosim/biosimspace:2023.1.1 openbiosim/biosimspace:latest
```

This does the tagging on the server (hub.docker.com).

See [this page](https://docs.docker.com/build/building/multi-platform/)
for more information on how to create multi-platform docker images.
