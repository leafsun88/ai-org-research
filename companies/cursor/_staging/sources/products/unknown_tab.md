---
company: "Anysphere"
research_key: CURSOR
type: products
source: "cursor.com"
title: "tab"
url: https://cursor.com/product/tab
date: unknown
fetched_at: 2026-04-20T17:55:46
credibility: S2-S4
evidence: E2-E3
chars: 6878
---

# tab

**Source**: https://cursor.com/product/tab
**Channel**: products

---

Next-action prediction

Tab anticipates where you're headed and suggests changes.

Download for macOS
⤓

Try mobile agent
→

This element contains an interactive demo for sighted users. It's a demonstration of Cursor's IDE showing AI-powered coding assistance features. The interface is displayed over a scenic painted landscape wallpaper, giving the demo an artistic backdrop.

Cursor

Get Cursor

Dashboard.tsx

SupportChat.tsx

"use client";

import React, { useState } from "react";
import Navigation from "./Navigation";
import SupportChat from "./SupportChat";

export default function Dashboard() {

 return (
 <div className="flex h-[600px] border rounded-lg overflow-hidden">
 <div className="w-64 border-r">
 </div>
 <div className="w-80 border-l">
 <SupportChat />
 </div>
 </div>
 );
}

"use client";

import React, { useState } from "react";
import Navigation from "./Navigation";
import SupportChat from "./SupportChat";

export default function Dashboard() {

 return (
 <div className="flex h-[600px] border rounded-lg overflow-hidden">
 <div className="w-64 border-r">
 </div>
 <div className="w-80 border-l">
 <SupportChat />
 </div>
 </div>
 );
}

Beyond autocomplete

Multi-line changes, cross-file jumps, refactors that ripple through your codebase.

Interactive demo with multiple windows showing Cursor's AI-powered features. The interface is displayed over a subtle, solid brand background.

Get Cursor

CommandMenu.tsx

App.tsx

import { Command } from "cmdk";

export function CommandMenu() {

 return (

 <Command>

 <Command.Input placeholder="Search..." />

 <Command.List>

 <Command.Item>Settings</Command.Item>

 <Command.Item>Profile</Command.Item>

 </Command.List>

 </Command>

 );

}

Tabto App.tsx

In-session context

Tab sees your current task, recent changes, and relevant files to make context-aware suggestions.

Interactive demo with multiple windows showing Cursor's AI-powered features. The interface is displayed over a subtle, solid brand background.

Get Cursor

import { prisma, type Invoice } from "@/lib/db";

import type { Stripe } from "stripe";

export const getInvoicesByCustomer = (customerId: string) =>

prisma.invoice.findMany({ where: { customerId } });

export const getInvoice = (id: string): Promise<Invoice | null> =>

prisma.invoice.findUnique({

 where: { id },

 include: { lineItems: true, customer: true, charges: true },

});

Proprietary model

Built exclusively for Cursor, trained with RL on the largest sample of real-world scenarios.

Interactive demo with multiple windows showing Cursor's AI-powered features. The interface is displayed over a subtle, solid brand background.

Get Cursor

import { z } from "zod";

export const userSchema = z.object({

 id: z.string().uuid(),

 email: z.string().email(),

 name: z.string().min(2).max(100),

 role: z.enum(["admin", "user", "guest"]),

 createdAt: z.date(),

});

Recent highlights

Introducing Cursor 2.0 and Composer

A new interface and our first coding model, both purpose-built for working with agents.

Product · Oct 29, 2025

Improving Cursor Tab with online RL

Our new Tab model makes 21% fewer suggestions while having 28% higher accept rate.

Research · Sep 12, 2025

1.5x faster MoE training with custom MXFP8 kernels

Achieving a 3.5x MoE layer speedup with a complete rebuild for Blackwell GPUs.

Research · Aug 29, 2025

View more posts →

Try Tab now.

Download for macOS
⤓

Try mobile agent
→

Next-action prediction

Tab anticipates where you're headed and suggests changes.

Download for macOS
⤓

Try mobile agent
→

This element contains an interactive demo for sighted users. It's a demonstration of Cursor's IDE showing AI-powered coding assistance features. The interface is displayed over a scenic painted landscape wallpaper, giving the demo an artistic backdrop.

Cursor

Get Cursor

Dashboard.tsx

SupportChat.tsx

"use client";

import React, { useState } from "react";
import Navigation from "./Navigation";
import SupportChat from "./SupportChat";

export default function Dashboard() {

 return (
 <div className="flex h-[600px] border rounded-lg overflow-hidden">
 <div className="w-64 border-r">
 </div>
 <div className="w-80 border-l">
 <SupportChat />
 </div>
 </div>
 );
}

"use client";

import React, { useState } from "react";
import Navigation from "./Navigation";
import SupportChat from "./SupportChat";

export default function Dashboard() {

 return (
 <div className="flex h-[600px] border rounded-lg overflow-hidden">
 <div className="w-64 border-r">
 </div>
 <div className="w-80 border-l">
 <SupportChat />
 </div>
 </div>
 );
}

Beyond autocomplete

Multi-line changes, cross-file jumps, refactors that ripple through your codebase.

Interactive demo with multiple windows showing Cursor's AI-powered features. The interface is displayed over a subtle, solid brand background.

Get Cursor

CommandMenu.tsx

App.tsx

import { Command } from "cmdk";

export function CommandMenu() {

 return (

 <Command>

 <Command.Input placeholder="Search..." />

 <Command.List>

 <Command.Item>Settings</Command.Item>

 <Command.Item>Profile</Command.Item>

 </Command.List>

 </Command>

 );

}

Tabto App.tsx

In-session context

Tab sees your current task, recent changes, and relevant files to make context-aware suggestions.

Interactive demo with multiple windows showing Cursor's AI-powered features. The interface is displayed over a subtle, solid brand background.

Get Cursor

import { prisma, type Invoice } from "@/lib/db";

import type { Stripe } from "stripe";

export const getInvoicesByCustomer = (customerId: string) =>

prisma.invoice.findMany({ where: { customerId } });

export const getInvoice = (id: string): Promise<Invoice | null> =>

prisma.invoice.findUnique({

 where: { id },

 include: { lineItems: true, customer: true, charges: true },

});

Proprietary model

Built exclusively for Cursor, trained with RL on the largest sample of real-world scenarios.

Interactive demo with multiple windows showing Cursor's AI-powered features. The interface is displayed over a subtle, solid brand background.

Get Cursor

import { z } from "zod";

export const userSchema = z.object({

 id: z.string().uuid(),

 email: z.string().email(),

 name: z.string().min(2).max(100),

 role: z.enum(["admin", "user", "guest"]),

 createdAt: z.date(),

});

Recent highlights

Introducing Cursor 2.0 and Composer

A new interface and our first coding model, both purpose-built for working with agents.

Product · Oct 29, 2025

Improving Cursor Tab with online RL

Our new Tab model makes 21% fewer suggestions while having 28% higher accept rate.

Research · Sep 12, 2025

1.5x faster MoE training with custom MXFP8 kernels

Achieving a 3.5x MoE layer speedup with a complete rebuild for Blackwell GPUs.

Research · Aug 29, 2025

View more posts →

Try Tab now.

Download for macOS
⤓

Try mobile agent
→
