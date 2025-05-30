# Download base image
FROM ghcr.io/linuxserver/mariadb

# candidates for customisation are
ENV CANDIDATES="/defaults/my.cnf /defaults/custom.cnf"

# apply stability patches recommended in
#   
#   https://discord.com/channels/638610460567928832/638610461109256194/825049573520965703
#   https://stackoverflow.com/questions/61809270/how-to-discover-why-mariadb-crashes
#   as at 2025-04-23, thread_cache_size is ignored (at least for MariaDB versions 10.6.9
#   through 11.4.5 where it always has the value 100). It could probably be removed.
RUN for CNF in ${CANDIDATES} ; do [ -f ${CNF} ] && break ; done ; \
    sed -i.bak \
        -e "s/^thread_cache_size/# thread_cache_size/" \
        -e "s/^read_buffer_size/# read_buffer_size/" \
        ${CNF}

# copy the health-check script into place
ENV HEALTHCHECK_SCRIPT="iotstack_healthcheck.sh"
COPY ${HEALTHCHECK_SCRIPT} /usr/local/bin/${HEALTHCHECK_SCRIPT}

# define the health check
HEALTHCHECK \
   --start-period=30s \
   --interval=30s \
   --timeout=10s \
   --retries=3 \
   CMD ${HEALTHCHECK_SCRIPT} || exit 1

ENV CANDIDATES=

# EOF

