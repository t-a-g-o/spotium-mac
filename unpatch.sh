# A modified version of BlocTheSpot for mac.
# https://github.com/Nuzair46/BlockTheSpot-Mac/tree/main

#!/usr/bin/env bash
APP_PATH="/Applications/Spotify.app"
PATH_FLAG='false'
while getopts 'P:' flag; do
  case "${flag}" in
  P)
    APP_PATH="${OPTARG}"
    PATH_FLAG='true'
    ;;
  *)
    echo "Error: Flag not supported."
    exit
    ;;
  esac
done
if [[ "${PATH_FLAG}" == 'false' ]]; then
  if [[ -d "${HOME}${APP_PATH}" ]]; then
    INSTALL_PATH="${HOME}${APP_PATH}"
  elif [[ -d "${APP_PATH}" ]]; then
    INSTALL_PATH="${APP_PATH}"
  else
    exit
  fi
else
  if [[ -d "${APP_PATH}" ]]; then
    INSTALL_PATH="${APP_PATH}"
  else
    exit
  fi
fi
XPUI_PATH="${INSTALL_PATH}/Contents/Resources/Apps"
XPUI_SPA="${XPUI_PATH}/xpui.spa"
XPUI_BAK="${XPUI_PATH}/xpui.bak"
APP_BINARY="${INSTALL_PATH}/Contents/MacOS/Spotify"
APP_BINARY_BAK="${INSTALL_PATH}/Contents/MacOS/Spotify.bak"
if [[ ! -f "${XPUI_BAK}" ]] || [[ ! -f "${APP_BINARY_BAK}" ]]; then
  exit 
fi
rm "${XPUI_SPA}"
rm "${APP_BINARY}"
mv "${XPUI_BAK}" "${XPUI_SPA}"
mv "${APP_BINARY_BAK}" "${APP_BINARY}"
exit