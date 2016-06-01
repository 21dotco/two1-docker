# 21: Bitcoin Micropayments over HTTP

![21 logo](docs/img/21_banner.png "21")

# What is `two1`?

`two1` consists of a command line tool and python3 library that enable you to build the [machine-payable web](https://21.co). Learn more at [https://21.co](https://21.co).

# Quickstart

## Try it

#### Pull the latest base image with `two1` installed:
``` bash
$ docker pull 21dotco/two1
```

#### Run the image:
``` bash
$ docker run -it 21dotco/two1 sh
```

#### Get started:
Run `21 help` to see the help menu, or `21 status` to get started. You can also use the [Kitematic](https://kitematic.com/) GUI to launch the `two1` images.  Search for `two1` and click to launch!

## Sell microservices for bitcoin

The images provided in this repository are designed to work with the `21 sell` service manager that is included with your installation of **21**.  [Sign up](https://21.co) to install `21` and learn more about the `21 sell` tool [here](https://21.co/learn/21-sell).

# Supported tags

## `base`

This is a base [Alpine Linux](http://www.alpinelinux.org/) image with the `two1` python3 libraries installed via pip.

## `router`

This is an Alpine Linux image with `nginx` added and used for routing to the individual microservices and payments server.

## `payments`

This is the payments server that manages the [payment channels](https://21.co/learn/intro-to-micropayment-channels) for all microservices in a `21 sell` deployment.

## `services-*`

All machine-payable microservices available for you to start selling are prefixed with the string `service-`.  For example, the `ping` microservice image tag `service-ping`.

# Supported Docker versions

These images are supported on Docker version `1.11.0` and up.

## Community

Join our [global development community](https://slack.21.co) to chat with other users or to get in touch with support.

# Licensing

`two1` is licensed under the FreeBSD License. See [LICENSE](https://github.com/21dotco/two1-python/blob/master/LICENSE) for the full license text. Please see our Terms of Use [here](https://21.co/terms-of-use).

# Issues

If you have any problems with or questions about these images, please contact
[support@21.co](mailto: support@21.co).
