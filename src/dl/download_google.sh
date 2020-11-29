#!/usr/bin/env bash

[[ -v VERBOSE ]] && set -x
set -eu

# This script lists all ip ranges currently used by
# the google cloud platform, according to ns-lookup / dig
# TXT _cloud-netblocks.googleusercontent.com
#
# https://cloud.google.com/compute/docs/faq#ipranges

errcho() {
    >&2 echo "$@"
}

_fmt() {
    echo "$1" | cut -f "$2" -d':'
}

_txt_recursive() {
    for txt_entry in $(dig txt "$1" +short | tr " " "\n"); do
        if [[ "${txt_entry}" == include:* ]]; then
            _txt_recursive "$(_fmt ${txt_entry} 2)"
        elif [[ "${txt_entry}" == ip4:* && "${ipv4}" == true ]]; then
            _fmt "${txt_entry}" 2
        elif [[ "${txt_entry}" == ip6:* && "${ipv6}" == true ]]; then
            _fmt "${txt_entry}" 2-9
        fi
    done
}

domain="_cloud-netblocks.googleusercontent.com"

ipv4=true
ipv6=true

while (( $# > 0 )); do
    case "$1" in
        --ipv4)
            ipv6=false
            shift 1
            ;;
        --ipv6)
            ipv4=false
            shift 1
            ;;
        --domain)
            domain="$2"
            shift 2
            ;;
        *)
            errcho "Unknown option $1"
            exit 1
            ;;
    esac
done

if [[ "${ipv4}" == false && "${ipv6}" == false ]]; then
    errcho "WARN: --ipv4 and --ipv6 options are mutually exclusive and will likely prevent output"
fi

_txt_recursive "${domain}"
