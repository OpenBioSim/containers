# Building Sire

This container is used to build sire on platforms that aren't supported
by GitHub Actions (e.g. Linux/ARM64), or to debug building for new
Python versions (e.g. not currently on our CI), or branches 
that are non-default (not main or devel).

Build using

```
docker build -t openbiosim/build_sire:latest \
  --platform {PLATFORM}
  --build-arg python_version={VERSION} --build-arg branch={BRANCH} .
```

where `{PLATFORM}` is the platform to build,
`{VERSION}` is the Python version, and `{BRANCH}` is the 
branch you want to build.

For example

```
docker build -t openbiosim/build_sire:latest \
  --platform linux/arm64 \
  --build-arg python_version=3.9 --build-arg branch=main .
```

would build the ARM64 package of the main branch for Python 3.9.

As with all compilation, it will take a time!

When it has finished, you can run the container to access the 
package, e.g.

```
docker run -it openbiosim/build_sire:latest
```

This will drop you into a bash session as user `openbiosim`.
The package was built in the directory `/home/openbiosim/build`.

From here, you can test the package and then decide whether
or not you want to upload it to conda-forge.
