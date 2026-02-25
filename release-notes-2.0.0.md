# ispy-webgl v2.0.0 Release Notes

## Breaking Changes

- jQuery removed
- Bootstrap upgraded from 3 to 5
- ES Modules & Vite — the project has been converted from vendored script tags to ES modules with a Vite-based build system; vendored libraries replaced with npm packages
- SVGRenderer removed — no longer supported as a rendering path

## Major Upgrades

- Three.js upgraded from r125 to r182
- JSZip upgraded from 2.x to 3.8.0

## New Features

- GLTF/GLB import support — users can now import local GLTF and GLB files
- AK4 and AK8 PF and PAT jet support
- CSC plus/minus geometries
- Packed candidate towers
- Display height slider — adjustable viewport height via slider
- Cursor feedback — cursor changes when highlighting rows in the event table

## Bug Fixes

- Fix muon-rphi-plus geometry
- Fix render order for imported geometries and physics objects
- Fix transparency behavior for muon chambers

## Infrastructure

- Added production build with static asset copying
- Added ESLint and pre-commit hooks for code quality enforcement
