#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 *is_palindrome- Checks if singly linked list is a palindrome.
 * 
 *@head:The head pointer
 *
 *Return: Returns 0 if it is not a palindrome, 
 * and 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int values[9999], a = 0, c = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	node = *head;
	if (!node->next)
	{
		return (1);
	}
	while (node)
	{
		values[a] = node->n;
		node = node->next;
		a++;
	}
	a--;
	while (a >= 0 && c <= a)
	{
		if (values[a] != values[c])
		{
			return (0);
		}
		a--;
		c++;
	}
	return (1);
}
