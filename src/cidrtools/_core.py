# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
CFFI bindings tp the *cidrtools* C-library (and structs)
"""
import cffi

ffi = cffi.FFI()

#
# The FFI bindings
#
ffi.cdef("""
    void free(void *ptr);

    struct in_addr {
        uint32_t s_addr;
    };
    struct in6_addr {
        uint8_t s6_addr[16];
    };

    typedef struct ct_address {
        int family;
        union {
            struct in_addr v4;
            struct in6_addr v6;
        } addr;
    } CtAddress;

    typedef struct ct_cidr {
        CtAddress addr;
        uint8_t prefix;
    } CtCidr;

    typedef struct ct_cidrs {
        CtCidr *blocks;
        size_t count;
    } CtCidrs;

    int ct_clean_cidrs(CtCidrs *cidrs);
    int ct_clean_cidr(CtCidr *cidr);
    bool ct_cidr_contains_ip(const CtCidr *cidr, const CtAddress *ip);
    bool ct_cidr_contains_cidr(const CtCidr *parent, const CtCidr *target);
    int ct_cidr_fix_host_bits(CtCidr *cidr);
    bool ct_cidr_is_subnet(const CtCidr *cidr, const CtCidrs *cidrs);
    int ct_cidr_to_range(const CtCidr *cidr, CtAddress *first, CtAddress *last);
    int ct_cidr_to_range_mid(const CtCidr *cidr, CtAddress *first, CtAddress *mid, CtAddress *last);
    char *ct_cidr_to_str(const CtCidr *cidr);
    int ct_cidr_to_str_r(const CtCidr *cidr, char *buf, size_t buflen);
    int ct_str_to_cidr_parts(const char *cidr, char *ip_addr, size_t ip_addr_len, uint8_t *prefix);
    int ct_compact(CtCidrs *cidrs);
    int ct_exclude_cidrs(CtCidrs *all, CtCidrs *excluded);
    char *ct_format_host_bits(const CtCidr *cidr);
    int ct_get_host_bits(const CtCidr *cidr, CtAddress *addr);
    bool ct_is_ipv4(const CtCidr *cidr);
    bool ct_is_ipv6(const CtCidr *cidr);
    size_t ct_num_ips(const CtCidr *cidr);
    int ct_range_to_cidrs(const CtAddress *first, const CtAddress *last, CtCidrs *cidrs);
    int ct_cidr_set_prefix(CtCidr *cidr, uint8_t prefix);
    int ct_sort(CtCidrs *cidrs);
    int ct_str_to_cidr_block(const char *str, CtCidr *cidr);
    CtCidrs *ct_subnets_split(const CtCidr *cidr, uint8_t prefix);
    char *ct_version(void);
    int ct_split_by_family(CtCidrs *cidrs, CtCidrs *cidrs_v4, CtCidrs *cidrs_v6);
    void ct_free_cidrs(CtCidrs *cidrs);
    bool ct_add_cidr_to_cidrs(CtCidrs *cidrs, const CtCidr *cidr);
    bool ct_allocate_cidrs(size_t count, CtCidrs *cidrs);

    int ct_str_array_to_cidrs(const char **str_array, size_t count, CtCidrs *cidrs);
    int ct_cidrs_to_str_array(const CtCidrs *cidrs, char **dest_array);

    int ct_flat_buffer_to_cidrs(const char *flat_str, size_t count, CtCidrs *cidrs);
    char *ct_cidrs_to_flat_buffer(const CtCidrs *cidrs);

    int ct_ip_address_increment(const CtAddress *addr, size_t num, CtAddress *addr_inc);
    int ct_ip_address_range(const CtAddress *addr, uint8_t prefix, CtAddress *first, CtAddress *last);
    char *ct_ip_address_to_str(const CtAddress *ip_addr);
    int ct_ip_address_to_str_r(const CtAddress *ip_addr, char *buf, size_t buflen);
    int ct_str_to_ip_address(const char *address, CtAddress *ip_addr);

    int ct_ip_str_to_hostname(const char *ip, char *hostname);
    int ct_hostname_to_address(const char *hostname, CtCidrs *cidrs);
""")

try:
    lib = ffi.dlopen("libcidrtools.so")
except OSError:
    lib = ffi.dlopen("./libcidrtools.so")
